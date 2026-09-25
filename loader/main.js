window.files = {};   // filename → { bytes: Uint8Array, edited: boolean }
window.currentFile = null;
window.editor = null;

function loadBase64(file, iframe) {
	// 'file' should be a Blob, File, or Uint8Array wrapped in a Blob
	const blob = file instanceof Blob ? file : new Blob([file]);

	const reader = new FileReader();
	reader.onload = function () {
		// Extract base64 and store in window.gameData
    console.log("got game data as b64");
		
    window.gameData = reader.result.split(",")[1];

    setTimeout(()=>{
    iframe.contentWindow.postMessage({ type: "setGameData", data: window.gameData }, "*")
    console.log("sent")
    },1000)



    
	};
	reader.readAsDataURL(blob);
}


function bootGame(iframe) {
	saveCurrentFile();

	const zipInput = {};
	for (const [name, file] of Object.entries(files)) zipInput[name] = file.bytes;
	const zipped = fflate.zipSync(zipInput, { level: 9 });
	const blob = new Blob([zipped]);


  loadBase64(blob, iframe)
}



/* ---------- Load Love ---------- */
document.getElementById("loadLove").addEventListener("click", () => {
  const loveLoad = document.getElementById("loadLove")
  const editorDiv = document.getElementById("editor");

  if (editorDiv.style.display !== "none") {
    loveLoad.textContent = "Back to Editor"
    editorDiv.style.display = "none";

    const viewer = document.createElement("iframe");
    viewer.id = "loveViewer";
    viewer.src = "love.html";
    viewer.style.width = "100%";
    viewer.style.height = "100%";
    viewer.style.border = "none";
    viewer.style.flex = 1;

    editorDiv.parentElement.appendChild(viewer);

    bootGame(viewer)
  } else {
    loveLoad.textContent = "Load Love";
    editorDiv.style.display = "block";
    const viewer = document.getElementById("loveViewer");
    if (viewer) viewer.remove();
    editor.layout();
  }
});

/* ---------- Monaco Setup ---------- */
require.config({ paths: { vs: "https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs" } });
require(["vs/editor/editor.main"], () => {
  editor = monaco.editor.create(document.getElementById("editor"), {
    value: "",
    language: "plaintext",
    automaticLayout: true,
    theme: "vs-dark"
  });
});

/* ---------- Build tree structure ---------- */
function buildTree(filePaths) {
  const tree = {};
  filePaths.forEach(path => {
    const parts = path.split("/").filter(Boolean);
    let node = tree;
    parts.forEach((part, idx) => {
      if (!node[part]) node[part] = { __children: {}, __isFile: idx === parts.length - 1 && !path.endsWith("/") };
      node = node[part].__children;
    });
  });
  return tree;
}

/* ---------- Render tree recursively with right-click, sorted ---------- */
function renderTree(node, container, path = "", openState = {}) {
  // Preserve current open/closed state
  const prevState = {};
  Array.from(container.children).forEach(child => {
    if (child.dataset && child.dataset.path) {
      prevState[child.dataset.path] = child.nextSibling?.style.display === "block";
    }
  });

  Object.entries(node)
    .sort(([aName, aInfo], [bName, bInfo]) => {
      // Folders first
      if (aInfo.__isFile !== bInfo.__isFile) return aInfo.__isFile ? 1 : -1;
      // Then alphabetical
      return aName.localeCompare(bName, undefined, { sensitivity: "base" });
    })
    .forEach(([name, info]) => {
      const item = document.createElement("div");
      item.className = "tree-item";
      const fullPath = path + name + (info.__isFile ? "" : "/");
      item.dataset.path = fullPath;

      if (info.__isFile) {
        if (name !== ".keep") {
          item.textContent = "📄 " + name;
          item.style.paddingLeft = "10px";
          item.onclick = () => openFile(fullPath);
          item.oncontextmenu = e => {
            e.preventDefault();
            showContextMenu(e.pageX, e.pageY, fullPath, false);
          };
          container.appendChild(item);
        }
      } else {
        item.textContent = "📁 " + name;
        item.style.paddingLeft = "10px";

        const childrenContainer = document.createElement("div");
        childrenContainer.style.marginLeft = "10px";

        // Restore previous open state if exists
        childrenContainer.style.display = prevState[fullPath] ? "block" : "none";

        item.onclick = () => {
          childrenContainer.style.display = childrenContainer.style.display === "none" ? "block" : "none";
        };

        item.oncontextmenu = e => {
          e.preventDefault();
          showContextMenu(e.pageX, e.pageY, fullPath, true);
        };

        container.appendChild(item);
        container.appendChild(childrenContainer);

        // Recurse
        renderTree(info.__children, childrenContainer, fullPath, openState);
      }
    });
}


/* ---------- Load ZIP (fflate) ---------- */
document.getElementById("zipInput").addEventListener("change", async e => {
  const file = e.target.files[0];
  if (!file) return;

  const buffer = await file.arrayBuffer();
  const zipData = new Uint8Array(buffer);
  const unzipped = fflate.unzipSync(zipData);

  files = {};
  currentFile = null;

  Object.entries(unzipped).forEach(([name, bytes]) => {
    files[name] = { bytes, edited: false };
  });

  rebuildTree();
});

/* ---------- Open File ---------- */
function openFile(name) {
  saveCurrentFile();
  currentFile = name;
  const decoder = new TextDecoder("utf-8");
  editor.setValue(decoder.decode(files[name].bytes));

  const ext = name.split(".").pop();
  monaco.editor.setModelLanguage(editor.getModel(), guessLanguage(ext));
}

/* ---------- Save current editor buffer ---------- */
function saveCurrentFile() {
  if (!currentFile) return;
  const encoder = new TextEncoder();
  files[currentFile].bytes = encoder.encode(editor.getValue());
  files[currentFile].edited = true;
}

/* ---------- Save ZIP ---------- */
document.getElementById("saveZip").addEventListener("click", () => {
  saveCurrentFile();
  const zipInput = {};
  for (const [name, file] of Object.entries(files)) zipInput[name] = file.bytes;
  const zipped = fflate.zipSync(zipInput, { level: 9 });
  const blob = new Blob([zipped], { type: "application/zip" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "edited.zip";
  a.click();
});

/* ---------- Language Guess ---------- */
function guessLanguage(ext) {
  return {
    js: "javascript",
    ts: "typescript",
    json: "json",
    html: "html",
    css: "css",
    md: "markdown",
    lua: "lua",
    py: "python"
  }[ext] || "plaintext";
}

/* ---------- Add / Remove File Buttons ---------- */
document.getElementById("addFile").addEventListener("click", () => {
  const fileName = prompt("Enter new file name:");
  if (!fileName) return;
  if (files[fileName]) return alert("File already exists!");
  files[fileName] = { bytes: new Uint8Array(), edited: true };
  openFile(fileName);
  rebuildTree();
});

/* ---------- Context Menu ---------- */
const contextMenu = document.createElement("div");
contextMenu.id = "contextMenu";
contextMenu.style.position = "absolute";
contextMenu.style.background = "#333";
contextMenu.style.color = "#fff";
contextMenu.style.padding = "5px 0";
contextMenu.style.display = "none";
contextMenu.style.zIndex = 1000;
contextMenu.style.borderRadius = "4px";
contextMenu.style.minWidth = "150px";
contextMenu.style.boxShadow = "0 2px 5px rgba(0,0,0,0.5)";
document.body.appendChild(contextMenu);

function hideContextMenu() { contextMenu.style.display = "none"; }

document.addEventListener("click", hideContextMenu);
document.addEventListener("contextmenu", e => { if (!e.target.classList.contains("tree-item")) hideContextMenu(); });

function showContextMenu(x, y, targetPath, isFolder) {
  contextMenu.innerHTML = "";

  const addFile = document.createElement("div");
  addFile.textContent = "Add File";
  addFile.style.padding = "5px 10px";
  addFile.style.cursor = "pointer";
  addFile.onclick = () => {
    hideContextMenu();
    const fileName = prompt("Enter new file name:");
    if (!fileName) return;
    const fullPath = isFolder ? targetPath + fileName : targetPath.replace(/[^\/]+$/, "") + fileName;
    if (files[fullPath]) return alert("File exists!");
    files[fullPath] = { bytes: new Uint8Array(), edited: true };
    rebuildTree();
  };
  contextMenu.appendChild(addFile);

  const addFolder = document.createElement("div");
  addFolder.textContent = "Add Folder";
  addFolder.style.padding = "5px 10px";
  addFolder.style.cursor = "pointer";
  addFolder.onclick = () => {
    hideContextMenu();
    const folderName = prompt("Enter folder name:");
    if (!folderName) return;
    const fullPath = isFolder ? targetPath + folderName + "/" : targetPath.replace(/[^\/]+$/, "") + folderName + "/";
    files[fullPath + ".keep"] = { bytes: new Uint8Array(), edited: true };
    rebuildTree();
  };
  contextMenu.appendChild(addFolder);

  const rename = document.createElement("div");
  rename.textContent = "Rename";
  rename.style.padding = "5px 10px";
  rename.style.cursor = "pointer";
  rename.onclick = () => {
    hideContextMenu();
    const newName = prompt("Enter new name:", targetPath.split("/").filter(Boolean).pop());
    if (!newName) return;
    renamePath(targetPath, newName);
    rebuildTree();
  };
  contextMenu.appendChild(rename);

  const remove = document.createElement("div");
  remove.textContent = "Delete";
  remove.style.padding = "5px 10px";
  remove.style.cursor = "pointer";
  remove.onclick = () => {
    hideContextMenu();
    if (!confirm(`Delete "${targetPath}"?`)) return;
    deletePath(targetPath);
    currentFile = currentFile && currentFile.startsWith(targetPath) ? null : currentFile;
    editor.setValue(currentFile ? editor.getValue() : "");
    rebuildTree();
  };
  contextMenu.appendChild(remove);

  contextMenu.style.left = x + "px";
  contextMenu.style.top = y + "px";
  contextMenu.style.display = "block";
}

/* ---------- Delete / Rename Helpers ---------- */
function deletePath(path) {
  Object.keys(files).forEach(key => { if (key === path || key.startsWith(path)) delete files[key]; });
}

function renamePath(oldPath, newName) {
  const isFolder = oldPath.endsWith("/");
  const basePath = oldPath.split("/").slice(0, -1).join("/") + (isFolder ? "/" : "");
  const newPath = basePath + newName + (isFolder ? "/" : "");
  const updated = {};
  Object.entries(files).forEach(([key, val]) => {
    if (key === oldPath || key.startsWith(oldPath)) updated[key.replace(oldPath, newPath)] = val;
    else updated[key] = val;
  });
  files = updated;
}

/* ---------- Rebuild Tree ---------- */
function rebuildTree() {
  const tree = buildTree(Object.keys(files));
  const container = document.getElementById("fileTree");
  container.innerHTML = "";
  renderTree(tree, container);
}

/* ---------- Expose decoded files to Terminal ---------- */
Object.defineProperty(window, '_loveFiles', {
  get() {
    if (window.currentFile && window.editor) {
      // flush any unsaved Monaco edits into files first
      const encoder = new TextEncoder();
      window.files[window.currentFile].bytes = encoder.encode(window.editor.getValue());
    }
    const out = {};
    const decoder = new TextDecoder('utf-8');
    for (const [name, file] of Object.entries(window.files)) {
      out[name] = decoder.decode(file.bytes);
    }
    return out;
  }
});