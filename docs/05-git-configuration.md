# 03. Git Configuration & Line Endings

## 📅 Date: 2025-11-29

## 📝 Summary
We configured Git to enforce UNIX-style line endings (LF) across the entire project, regardless of the developer's operating system. This prevents syntax errors when executing scripts on the Linux server that were edited on Windows.

## ⚙️ Technical Details

### The Problem: CRLF vs LF
- **Windows** uses Carriage Return + Line Feed (`\r\n` or CRLF) for line breaks.
- **Linux** uses Line Feed (`\n` or LF).
- **Impact:** Bash scripts created or edited on Windows often fail on Linux with errors like `/bin/bash^M: bad interpreter` because the interpreter reads the invisible `\r` character as part of the command.

### The Solution: `.gitattributes`
Instead of relying on local user configuration (`core.autocrlf`), we implemented a repository-level rule using a `.gitattributes` file.

- **Rule:** `* text=auto eol=lf`
- **Effect:**
    1.  When files are checked out on Windows, they might appear as LF (modern editors like VS Code handle this perfectly).
    2.  When files are committed, Git guarantees they are stored as LF.
    3.  Exceptions were made for Windows-specific scripts (`.bat`, `.ps1`) to retain CRLF if needed.

### Implementation
We ran `git add --renormalize .` to immediately convert any existing files in the index to the new format.