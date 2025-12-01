# 13. Troubleshooting: Dashy OOM Error

## 📅 Date: 2025-12-01

## 📝 Summary
The initial deployment of Dashy failed due to a "JavaScript heap out of memory" error during the startup build process.

## ⚙️ Technical Analysis
- **Symptom:** Container loops with `FATAL ERROR: Reached heap limit Allocation failed`.
- **Root Cause:** The Node.js process inside the container defaulted to a heap limit of ~512MB. The frontend build process (Webpack/Vue CLI) requires more memory than this default, causing it to crash despite the Docker container having a 1GB limit.
- **Resolution:**
    1.  **Environment Variable:** Added `NODE_OPTIONS=--max-old-space-size=2048` to strictly define the heap size at 2GB.
    2.  **Container Limit:** Increased Docker resource limit (`deploy.resources.limits.memory`) from 1GB to 2GB to accommodate the larger heap.