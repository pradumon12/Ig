# 🚀 Instagram Profile Scraper

A powerful Python script that uses **Instaloader** to fetch publicly available Instagram profile data 📸.

---

## 🎯 Features
✅ **Fetches Instagram Profile Details**  
- 🆔 **Username**  
- 🏷 **Full Name**  
- 📜 **Bio**  
- 🌎 **Profile Picture URL**  
- 📊 **Followers & Following Count**  
- 📸 **Post Count**  
- ✅ **Verified Status**  
- 🏢 **Business Category (if applicable)**  
- 🔗 **External Website Link**  

✅ **Fetches Latest Post Caption** *(for public accounts)*  
✅ **Error Handling** *(No crashes for invalid usernames or private profiles)*  
✅ **Continuous Loop** *(Check multiple profiles in one session!)*  

---

## 🛠 Installation
Make sure you have **Python** installed, then install `instaloader` using:  
```bash
pip install instaloader
```
---
## 🚀 Usage

1️⃣ Clone the repository
```bash
git clone https://github.com/pradumon12/instagram-profile-scraper.git
cd instagram-profile-scraper
```
2️⃣ Run the script
```bash
python scraper.py
```
3️⃣ Enter an Instagram username and view profile details.
4️⃣ Type exit to quit the program.
## ❗ EXAMPLE 
```bash
Enter Instagram Username: pradumon14

==================================================
Username        : pradumon14
Full Name       : Pradumon Sahni
Biography       : Cool coder 
Profile Pic URL : https://instagram.com/xyz/profile.jpg
Posts Count     : 15000
Followers       : 26500000
Following       : 120
Private Account : No
Verified        : Yes
External URL    : https://www.example.com
Business Category: No

Recent Post Caption:
- Learning Mahine learning
```
---

⚠ Limitations

❌ Does NOT fetch private profile details or posts
❌ Excessive requests may result in temporary IP blocking by Instagram


---

📌 To-Do List

🔐 Add login support for extended access

💾 Save fetched data into a file

📊 Create a GUI version

---
