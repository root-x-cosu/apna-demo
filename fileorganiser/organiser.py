import os
import shutil

def organize_files(directory):
    # File categories
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac', '.aac'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Code': ['.py', '.java', '.cpp', '.js', '.html']
    }
    
    print(f"\n📁 Organizing: {directory}\n")
    
    # Create folders
    for folder in categories.keys():
        path = os.path.join(directory, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"✅ Created: {folder}/")
    
    # Create Others folder
    others = os.path.join(directory, 'Others')
    if not os.path.exists(others):
        os.makedirs(others)
        print(f"✅ Created: Others/")
    
    print("\nMoving files...\n")
    
    # Get files
    try:
        items = os.listdir(directory)
        files = [f for f in items if os.path.isfile(os.path.join(directory, f))]
    except:
        print("❌ Error reading directory!")
        return
    
    moved = 0
    
    # Move files
    for file in files:
        if file == 'organizer.py':
            continue
            
        ext = os.path.splitext(file)[1].lower()
        
        file_moved = False
        for category, extensions in categories.items():
            if ext in extensions:
                src = os.path.join(directory, file)
                dst = os.path.join(directory, category, file)
                try:
                    shutil.move(src, dst)
                    print(f"  ➜ {file} → {category}/")
                    moved += 1
                    file_moved = True
                    break
                except:
                    print(f"  ❌ Error: {file}")
        
        if not file_moved:
            src = os.path.join(directory, file)
            dst = os.path.join(directory, 'Others', file)
            try:
                shutil.move(src, dst)
                print(f"  ➜ {file} → Others/")
                moved += 1
            except:
                pass
    
    print(f"\n✅ Done! Moved {moved} files\n")

if __name__ == "__main__":
    organize_files("./test_files")