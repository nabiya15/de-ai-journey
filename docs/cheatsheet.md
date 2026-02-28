# 🛠️ Data Engineering Quick Reference (2026)

## 🌿 Git & Version Control
| Command | Purpose |
| :--- | :--- |
| `git status` | Check which files are changed/staged. |
| `git add .` | Stage all changes for commit. |
| `git commit -m "feat: message"` | Save changes locally with a descriptive message. |
| `git push origin main` | Upload local changes to GitHub. |
| `git pull origin main` | Fetch and merge latest changes from GitHub. |
| `git checkout -b branch-name` | Create a new "Feature Branch" for safe testing. |

## 🐍 Python for Ingestion (Module 01)
**The "Requests" Template:**
```python
import requests
response = requests.get('[https://api.example.com/data](https://api.example.com/data)')
if response.status_code == 200:
    data = response.json() # Converts web data to a Python Dictionary
```

## Pandas Quick-Cleaning:
- df.dropna(): Remove missing values.
- df.fillna(0): Replace nulls with zeros.
- df.astype(float): Convert columns to numbers.
- df.drop_duplicates(): Remove repeat records.

## 💾 SQL for Transformation (Module 03)
```SQL
WITH clean_data AS (
    SELECT id, UPPER(status) as status
    FROM raw_table
    WHERE temp IS NOT NULL
)
SELECT * FROM clean_data;

```
### Window Function (The "Interview King"):
```SQL
SELECT 
    id, 
    temp, 
    RANK() OVER (PARTITION BY sensor_id ORDER BY temp DESC) as temp_rank
FROM sensor_readings;

```

---

### **How to "Pin" this for Maximum Handiness**
Once you've pushed this to GitHub:
1.  **Browser Pin:** Open `docs/CHEATSHEET.md` on GitHub, copy the URL, and add it to your browser's **Bookmarks Bar**.
2.  **Repo Shortcut:** Add a link at the very top of your main `README.md`:
    > 💡 **Quick Links:** [Syllabus](Syllabus.md) | [Cheat Sheet](docs/CHEATSHEET.md) | [Sprint Board](https://github.com/users/nabiya15/projects/5)
3.  **Cursor Sidebar:** In Cursor, you can keep the `CHEATSHEET.md` tab **"Pinned"** (Right-click the tab > Pin) so it never disappears when you open new files.

**Would you like me to help you add the link to your Sprint Board into that README "Quick Links" section now?**

---
[Git Ultimate Cheat Sheet for 2026](https://www.youtube.com/shorts/mMBDBSIP3yk)

This video is a rapid-fire reference for the exact Git commands we just added to your cheat sheet, making it a great visual refresher if you ever get stuck on a command line error.


http://googleusercontent.com/youtube_content/10