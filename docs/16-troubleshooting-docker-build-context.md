# 16. Troubleshooting: Docker Build Context

## 📅 Date: 2025-12-02

## 📝 Summary
We encountered a `failed to calculate checksum` error during the Docker build process. The build failed because the `Dockerfile` attempted to copy `requirements.txt` from the root context, while the file actually resided in the `app/` subdirectory.

## ⚙️ The Fix: Correcting Build Context
Instead of complicating the paths inside the Dockerfile (e.g., `COPY app/requirements.txt .`), we adopted a cleaner architecture:

1.  **Moved Dockerfile:** Relocated `Dockerfile` into the `app/` directory. This encapsulates the application logic, dependencies, and build instructions in a single unit.
2.  **Updated Compose:** Changed the build context in `docker-compose.yml` from `.` to `./app`.

### Why this is better?
This makes the `app` folder portable. If we ever want to move this Python application to another repository or deploy it independently, it has everything it needs inside its own folder, without depending on files in the parent directory.