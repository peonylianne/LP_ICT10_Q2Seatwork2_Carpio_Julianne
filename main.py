from pyscript import document

def compute_average(event):
    # Get student's name
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    # Get scores
    try:
        score1 = float(document.getElementById("score1").value)
        score2 = float(document.getElementById("score2").value)
        score3 = float(document.getElementById("score3").value)
        score4 = float(document.getElementById("score4").value)
        score5 = float(document.getElementById("score5").value)
        score6 = float(document.getElementById("score6").value)
    except ValueError:
        document.getElementById("average").innerText = "Invalid input"
        document.getElementById("result").innerText = ""
        document.getElementById("gradeSummary").innerText = "Please enter valid numbers for all scores."
        return

    average = (score1 + score2 + score3 + score4 + score5 + score6) / 6


    if average >= 75:
        result = "Pass" 
    else:
        result = "Fail" 

    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result

    summary_text = f"{first_name} {last_name}'s Grade Summary:<br>" \
                   f"Science: {score1}<br>" \
                   f"Math: {score2}<br>" \
                   f"English: {score3}<br>" \
                   f"Filipino: {score4}<br>" \
                   f"ICT: {score5}<br>" \
                   f"PE: {score6}<br>" \
                   f"Overall Average: {round(average, 2)}<br>" \
                   f"Status: {result}"
    document.getElementById("gradeSummary").innerHTML = summary_text