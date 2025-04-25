"""
Fresh start for the Hospital Management System application.
This script ensures all caches are cleared before starting.
"""
import os
import sys
import shutil
import importlib
import uvicorn

def clear_caches():
    """Clear all __pycache__ directories in the project."""
    print("Clearing Python cache files...")
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            cache_dir = os.path.join(root, '__pycache__')
            print(f"Removing {cache_dir}")
            shutil.rmtree(cache_dir, ignore_errors=True)
    
    print("Clearing sys.modules cache...")
    to_remove = [m for m in sys.modules if m.startswith('hospital')]
    for module_name in to_remove:
        print(f"Removing {module_name} from sys.modules")
        sys.modules.pop(module_name, None)
    
    # Ensure FastAPI modules are also reloaded
    fastapi_modules = [m for m in sys.modules if m.startswith('fastapi')]
    for module_name in fastapi_modules:
        print(f"Removing {module_name} from sys.modules")
        sys.modules.pop(module_name, None)
    
    print("Cache clearing complete.")

if __name__ == "__main__":
    # Clear all caches first
    clear_caches()
    
    # Now import the app
    from hospital.entrypoints.main import app
    
    # Print instructions
    print("\n===== BROWSER CACHE INSTRUCTIONS =====")
    print("If you still see outdated API docs in Swagger UI:")
    print("1. Try opening the app in a private/incognito window")
    print("2. OR clear your browser cache manually:")
    print("   - Chrome: Press Ctrl+Shift+Delete")
    print("   - Firefox: Press Ctrl+Shift+Delete")
    print("   - Edge: Press Ctrl+Shift+Delete")
    print("3. OR force refresh with Ctrl+F5")
    print("====================================\n")
    
    # Run the app with a specific port to avoid any conflicts
    print("Starting fresh instance of the app...")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=False) 