from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic (same as your JS)
def get_bot_reply(user_message):
    q = user_message.lower()

    if "course" in q or "programme" in q:
        return "KU offers B.Tech (CSE, ECE, EEE, Pharma), BBA, MBA, MCA, M.Tech, BCA, B.Com & more."
    elif "eligibility" in q:
        return "UG: 45% in 12th with KCET/JEE; PG: 50% in graduation with entrance like PGCET/CAT."
    elif "about college" in q:
        return "Basavarajeswari Group of Institutions governed by Tungabhadra Education Health & Rural Development (TEHRD) Trust® is recognized one among the value-based quality oriented and inclusive educational groups in the country. The Trust® governed by qualified professionals endeavours to impart quality education to all the cross section of the society. The TEHRD Trust® is imparting quality education to more than 11,000 students in Ballari.Kishkinda University is a state private University, which has been established in Karnataka state with TEHRD – Trust® as the sponsoring body through the Karnataka State Act. No. 20 of 2023 and passed by the Karnataka Legislature."    
    elif "fee" in q:
        return "Fees vary by course. Please check the admissions section or contact admin for details."
    elif "hostel" in q or "transport" in q:
        return "Yes! KU provides separate hostels for boys and girls, and local transport facilities."
    elif "placement" in q:
        return "KU has 854+ placements in 2023-24. Avg package: ₹4.5 LPA, Highest: ₹19.5 LPA."
    elif "recruiter" in q or "company" in q:
        return "Top recruiters: TCS, Infosys, Wipro, Tech Mahindra, Accenture, Cognizant, HDFC, and more."
    elif "location" in q or "campus" in q:
        return "KU is located in Hanumanahalli, Ballari District, Karnataka."
    elif "scholarship" in q:
        return "Yes, KU offers merit-based and need-based scholarships. Check the official site."
    elif "library" in q or "lab" in q or "facility" in q:
        return "Modern labs, smart classrooms, Wi-Fi campus, digital library, auditorium, gym, sports & more."
    elif "contact" in q or "phone" in q:
        return "Call the admission cell: +91-94490-86655 or email info@kishkindauniversity.edu.in"
    elif "ugc" in q or "aicte" in q or "approval" in q:
        return "Yes, Kishkinda University is recognized by UGC and has AICTE-approved programs."
    elif "international" in q or "collaboration" in q or "global" in q:
        return "KU collaborates with global universities for student exchange and research programs."
    elif "how many" in q and "branches" in q:
        return "Kishkinda University has over 6 academic branches including Engineering, Management, Commerce, Pharmacy, Computer Applications, and Science."
    elif "undergraduate" in q or "ug courses" in q:
        return "UG courses include B.Tech (CSE, EEE, ECE, Pharma), BCA, BBA, and B.Com."
    elif "postgraduate" in q or "pg courses" in q:
        return "PG courses include MBA, MCA, and M.Tech in various specializations."
    elif "specialization" in q and "b.tech" in q:
        return "B.Tech specializations include CSE, AI & ML, EEE, ECE, and Pharmaceutical Engineering."
    elif "department" in q or "b.tech" in q:
        return "CSE,EEE,EC,BCA,MCA,MBA and MTECH"
    elif "about cse" in q or "cse" in q:
        return "There are totaly 240 seats and fees 1,25,000/"
    elif "diploma" in q or "certification" in q:
        return "Currently, KU focuses on full-time degree programs. For diploma options, check with the admissions cell."
    elif "integrated" in q or "dual degree" in q:
        return "Yes! KU offers integrated BBA + MBA and other programs. Contact admissions for more info."
    elif "pharmacy" in q or "pharma" in q:
        return "KU offers B.Tech in Pharmaceutical Engineering and research opportunities in the pharma domain."
    elif "faculty" in q or "professor" in q or "teacher" in q:
        return "Here are some of our faculty members: Dr. Rajshree V. Bivadar (HOD), Dr. Shivkumar, Dr. Mivakeshi,Mr. Vannur Swamy,Mr. Mujeeb Ansari,Mrs. Anitha Jyothi,Mrs. Deepa T,Mr. Quadri,Mr. Ganesh,Mrs. Ashwini."
    elif "extra activities" in q or "Extra Activities" in q:
        return "1.Clubs and Chapters 2.Tech Work Shops 3.SDP and FDP 4.Internship and Scholoarship 5.Industrial Visit."
    elif "Admission Section" in q or "admission section" in q:
        return "1.CSE -240 seats,1,25,000/fees 2.EC -120 seats,1,25,000/fees"
    else:
        return "Sorry, I didn’t understand that. Please ask about courses, placements, hostel, fees, etc."


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = get_bot_reply(user_input)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)