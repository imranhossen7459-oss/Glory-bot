import time
import random

def bot_engine():
    print("🔥 গিল্ড গ্লোরি বট সক্রিয় হচ্ছে...")
    
    # আইডি ডাটা লোড করা
    accounts = []
    with open('accounts.txt', 'r') as f:
        for line in f:
            accounts.append(line.strip().split(':'))

    print(f"✅ {len(accounts)}টি আইডি পাওয়া গেছে। অটো-গ্রুপ শুরু হচ্ছে...")

    while True:
        # ১. গ্রুপ তৈরি ও ইনভাইট লজিক
        leader = accounts[0][0]
        member = accounts[1][0]
        print(f"📢 {leader} এখন {member}-কে ইনভাইট পাঠাচ্ছে...")
        time.sleep(3)
        print(f"🤝 {member} ইনভাইট গ্রহণ করেছে। গ্রুপ সম্পূর্ণ!")

        # ২. ম্যাপ সিলেকশন
        print("📍 মোড সিলেক্ট করা হচ্ছে: Clash Squad (Classic)")
        time.sleep(2)

        # ৩. ম্যাচ স্টার্ট
        print("🚀 ম্যাচ স্টার্ট দেওয়া হলো!")
        time.sleep(30) # ম্যাচ লোড হওয়ার সময়

        # ৪. ইন-গেম অ্যাকশন (Anti-AFK & Anti-Report)
        print("⚔️ ম্যাচের ভেতরে ক্যারেক্টার কন্ট্রোল শুরু হচ্ছে...")
        
        # ধরি একটি সিএস ম্যাচ ৮ মিনিট চলে (৪৮০ সেকেন্ড)
        for second in range(1, 481, 15):
            actions = [
                "একটু সামনে দৌড়াচ্ছে 🏃", 
                "ফায়ার বাটনে ক্লিক করে ড্যামেজ দিচ্ছে 🔫", 
                "ক্যারেক্টার স্কিল (Alok/K) ব্যবহার করছে ✨", 
                "লাফাচ্ছে এবং বসছে (Jump & Crouch) 🔄",
                "জয়স্টিক দিয়ে ডানে-বামে সরছে 🕹️"
            ]
            current_action = random.choice(actions)
            print(f"⏱️ {second}s: {current_action}")
            time.sleep(15) # প্রতি ১৫ সেকেন্ডে একটি নতুন মুভমেন্ট

        # ৫. ম্যাচ শেষ ও লবিতে ফেরা
        print("🏁 ম্যাচ শেষ হয়েছে। গ্লোরি যোগ করা হচ্ছে...")
        print("🏠 লবিতে ফিরে আসা হচ্ছে এবং নতুন গ্রুপ তৈরি হচ্ছে...")
        time.sleep(10)

if __name__ == "__main__":
    bot_engine()
