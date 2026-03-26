import subprocess
import os
import sys

def run_validation():
    print(f"--- Starting PrED Pipeline Validation (Python {sys.version.split()[0]}) ---")
    
    # 1. Define the test command
    # We use a small image size (640) and high confidence (0.5) 
    # just to verify the 'plumbing' works quickly.
    test_cmd = [
        "python", "pred_detect_sort.py",
        "--weights", "weights/best.pt",
        "--source", "sample_video.mp4",
        "--imgsz", "640",
        "--conf", "0.5"
    ]
    
    # 2. Execute the script
    try:
        # shell=False is safer; capture_output lets us see errors if it fails
        result = subprocess.run(test_cmd, capture_output=True, text=True, check=True)
        print("✅ Success: pred_detect_sort.py executed without errors.")
        print("Terminal Output Snippet:")
        print("\n".join(result.stdout.splitlines()[-5:])) # Show the last 5 lines of success
        
    except subprocess.CalledProcessError as e:
        print("❌ FAILED: The PrED model crashed during validation.")
        print("-" * 40)
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        print("-" * 40)
        sys.exit(1) # Tell GitHub Actions the test failed

if __name__ == "__main__":
    # Quick check: does the video and weights exist?
    if not os.path.exists("weights/best.pt"):
        print("⚠️ Error: weights/best.pt not found. Check your folder structure.")
        sys.exit(1)
    if not os.path.exists("sample_video.mp4"):
        print("⚠️ Error: sample_video.mp4 not found in root.")
        sys.exit(1)
        
    run_validation()
