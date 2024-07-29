import random

questions = {
    'What Does "CPU" Stands for? ': [
        "Central Processing Unit", 
        "Control Power Unit", 
        "Central Power Unit", 
        "Core Power Utility"
    ],
    'What Does "RAM" Stands for? ': [
        "Random Access Memory", 
        "Readily Available Memory", 
        "Read Access Memory", 
        "Random Allocation Memory"
    ],
    'What Does "ROM" Stands for? ': [
        "Read Only Memory", 
        "Read Often Memory", 
        "Random Only Memory", 
        "Run Only Memory"
    ],
    'What Does "URL" Stands for? ': [
        "Uniform Resource Locator", 
        "Uniform Resource Link", 
        "Uniform Resource Library", 
        "Universal Resource Locator"
    ],
    'What Does "HTTP" Stands for? ': [
        "Hypertext Transfer Protocol", 
        "Hyperlink Transfer Protocol", 
        "Hypertext Transmission Protocol", 
        "Hypertext Transfer Program"
    ],
    'What Does "HTML" Stands for? ': [
        "Hypertext Markup Language", 
        "Hyperlink Text Markup Language", 
        "Hypertext Markdown Language", 
        "Hypertext Marking Language"
    ],
    'What Does "SQL" Stands for? ': [
        "Structured Query Language", 
        "Standard Query Language", 
        "Structured Question Language", 
        "Sequential Query Language"
    ],
    'What Does "CSS" Stands for? ': [
        "Cascading Style Sheets", 
        "Computer Style Sheets", 
        "Cascading System Sheets", 
        "Creative Style Sheets"
    ],
    'What Does "OS" Stands for? ': [
        "Operating System", 
        "Open System", 
        "Operational System", 
        "Operating Software"
    ],
    'What Does "IP" Stands for? ': [
        "Internet Protocol", 
        "Internal Protocol", 
        "Internet Program", 
        "Internal Program"
    ],
    'What Does "BIOS" Stands for? ': [
        "Basic Input Output System", 
        "Binary Input Output System", 
        "Basic Input Output Software", 
        "Basic Internal Output System"
    ],
    'What Does "PDF" Stands for? ': [
        "Portable Document Format", 
        "Printable Document Format", 
        "Portable Data Format", 
        "Printable Data Format"
    ],
    'What Does "USB" Stands for? ': [
        "Universal Serial Bus", 
        "Universal System Bus", 
        "Universal Standard Bus", 
        "Universal Storage Bus"
    ],
    'What Does "WiFi" Stands for? ': [
        "Wireless Fidelity", 
        "Wireless File", 
        "Wireless Finder", 
        "Wireless Fix"
    ],
    'What Does "LAN" Stands for? ': [
        "Local Area Network", 
        "Large Area Network", 
        "Local Access Network", 
        "Long Area Network"
    ],
    'What Does "WAN" Stands for? ': [
        "Wide Area Network", 
        "World Area Network", 
        "Wide Access Network", 
        "Wide Array Network"
    ],
    'What Does "VGA" Stands for? ': [
        "Video Graphics Array", 
        "Visual Graphics Array", 
        "Video Graphics Adapter", 
        "Visual Graphics Adapter"
    ],
    'What Does "GUI" Stands for? ': [
        "Graphical User Interface", 
        "Graphical Unit Interface", 
        "General User Interface", 
        "Graphical User Interaction"
    ],
    'What Does "MAC" Stands for? ': [
        "Media Access Control", 
        "Media Access Computer", 
        "Main Access Control", 
        "Main Access Computer"
    ],
    'What Does "DOS" Stands for? ': [
        "Disk Operating System", 
        "Digital Operating System", 
        "Data Operating System", 
        "Disk Operating Software"
    ]
}

def shuffle_questions(questions):
    items = list(questions.items())
    random.shuffle(items)
    shuffled_questions = dict(items)
    return shuffled_questions

# Example usage:
shuffled_questions = shuffle_questions(questions)
