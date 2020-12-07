from tkinter import * 
import re
import json
"""
dictionary documenting each supported mutation 
* key = gene name (because the user will input the gene name) 
* value = list containing various properties of the specific mutation related to the key
    - each property explained ahead 
"""
gene_regex = re.compile(r"\d| ") # regex to ignore all number during sequence input
gene_dict = {
    # gene: [mutation name, point mutation, letter at point mutation, index of point mutation (starting with 1)]
    "hbb": ["Sickle-cell Anemia", "point", "t", 65],

    # gene: [mutation name, point mutation, letter at point mutation, index of point mutation (starting with 1)]
    "f8": ["Hemophilia A", "point", "a", 191799],

    # gene: [mutation name, insertion mutation, sequence inserted, index where exon starts, index where exon finishes,
    # normal number of "cag" sequences]
    "htt": ["Huntington's Disease", "insertion", "cag", 5001, 5414, 28],

    # gene: [mutation name, deletion mutation, normal number of characters in gene sequence, length of exon omitted]
    "hba1": ["Alpha Thalassemia", "deletion", 7872, 830]
}



# initializing json
with open('sequence.json', encoding='utf8') as f: 
    data = json.load(f)


# Create tkinter window
window = Tk()
window.title("Mutamind")
# Windo configuration
window.geometry("500x500")
window.configure(bg="white")

# making sure only 
gene_data = StringVar()
sequence_data = StringVar()

# Create text in tkinter window
gene_label = Label(window, text="Enter Gene", font=("Couier", 16)).pack(pady=10)
gene_textbox = Entry(window, textvariable=gene_data, width=50).pack(pady=10)
sequence_label = Label(window, text="Enter Sequence: ", font=("Couier", 16)).pack(pady=10)
sequence_textbox = Entry(window, textvariable=sequence_data, width=50).pack(pady=10)
note_label = Label(window, text="We only support HBB and HBA1 genes as of now.\n HTT and F8 are available only for high-end processors.", font=("Couier", 16)).pack(pady=30)

# saving user's entry data 
def getData():
    global gene
    global gene_sequence
    gene = gene_data.get()
    gene_sequence = sequence_data.get()
    gene_sequence = re.sub(gene_regex, "", gene_sequence)
    main()

# showing data for the the specific disease to a newwindow
def SickleCell():
    newWindow = Toplevel()
    newWindow.geometry('700x700')
    newWindow.title("Sickle Cell Anemia")   
# going through the JSON database
    mutation_name = data['sickle cell anemia']['name']
    mutation_info = data['sickle cell anemia']['info']
    mutation_symptomps = data['sickle cell anemia']['symptomps']
    mutation_treatments = data['sickle cell anemia']['treatments']
    mutation_name_label = Label(newWindow, text=mutation_name, font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_info_sentence = Label(newWindow, text=mutation_info, font=("Couier", 16)).pack(pady=10)
    mutation_symptomps_label = Label(newWindow, text="Symptoms: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_symptomps_sentence = Label(newWindow, text=mutation_symptomps, font=("Couier", 16)).pack(pady=10)
    mutation_treatments_label =  Label(newWindow, text="Treatments: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_treatments_setence = Label(newWindow, text=mutation_treatments, font=("Couier", 16)).pack(pady=10)
    warning = Label(newWindow, fg="red", text="WARNING: SEEK HELP IF ANY OF THESE SYMPTOMS APPLY TO YOU!", font=("Couier", 16, 'bold')).pack(pady=100)

# showing data for the the specific disease to a newwindow
def HemophiliaA():
    newWindow1 = Toplevel()
    newWindow1.geometry('700x700')
    newWindow1.title("Hemophilia A")   
# going through the JSON database
    mutation_name = data['hemophilia A']['name']
    mutation_info = data['hemophilia A']['info']
    mutation_symptomps = data['hemophilia A']['symptomps']
    mutation_treatments = data['hemophilia A']['treatments']
    mutation_name_label = Label(newWindow1, text=mutation_name, font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_info_sentence = Label(newWindow1, text=mutation_info, font=("Couier", 16)).pack(pady=10)
    mutation_symptomps_label = Label(newWindow1, text="Symptoms: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_symptomps_sentence = Label(newWindow1, text=mutation_symptomps, font=("Couier", 16)).pack(pady=10)
    mutation_treatments_label =  Label(newWindow1, text="Treatments: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_treatments_setence = Label(newWindow1, text=mutation_treatments, font=("Couier", 16)).pack(pady=10)
    warning = Label(newWindow1, fg="red", text="WARNING: SEEK HELP IF ANY OF THESE SYMPTOMS APPLY TO YOU!", font=("Couier", 16, 'bold')).pack(pady=10)
    
# showing data for the the specific disease to a newwindow
def HuntingtonsDisease():
    newWindow2 = Toplevel()
    newWindow2.geometry('700x700')
    newWindow2.title("Huntington's Disease")   
# going through the JSON database
    mutation_name = data['huntington’s disease']['name']
    mutation_info = data['huntington’s disease']['info']
    mutation_symptomps = data['huntington’s disease']['symptomps']
    mutation_treatments = data['huntington’s disease']['treatments']
    mutation_name_label = Label(newWindow2, text=mutation_name, font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_info_sentence = Label(newWindow2, text=mutation_info, font=("Couier", 16)).pack(pady=10)
    mutation_symptomps_label = Label(newWindow2, text="Symptoms: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_symptomps_sentence = Label(newWindow2, text=mutation_symptomps, font=("Couier", 16)).pack(pady=10)
    mutation_treatments_label = Label(newWindow2, text="Treatments: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_treatments_setence = Label(newWindow2, text=mutation_treatments, font=("Couier", 16)).pack(pady=10)
    warning = Label(newWindow2, fg="red", text="WARNING: SEEK HELP IF ANY OF THESE SYMPTOMS APPLY TO YOU!", font=("Couier", 16, 'bold')).pack(pady=10)

# showing data for the the specific disease to a newwindow
def AlphaThalassemia():
    newWindow2 = Toplevel()
    newWindow2.geometry('700x700')
    newWindow2.title("Huntington's Disease")   
# going through the JSON database
    mutation_name = data['Alpha Thalassemia']['name']
    mutation_info = data['Alpha Thalassemia']['info']
    mutation_symptomps = data['Alpha Thalassemia']['symptomps']
    mutation_treatments = data['Alpha Thalassemia']['treatments']
    mutation_name_label = Label(newWindow2, text=mutation_name, font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_info_sentence =Label(newWindow2, text=mutation_info, font=("Couier", 16)).pack(pady=10)
    mutation_symptomps_label = Label(newWindow2, text="Symptoms: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_symptomps_sentence = Label(newWindow2, text=mutation_symptomps, font=("Couier", 16)).pack(pady=10)
    mutation_treatments_label =  Label(newWindow2, text="Treatments: ", font=("Couier", 20, 'bold')).pack(pady=10)
    mutation_treatments_setence = Label(newWindow2, text=mutation_treatments, font=("Couier", 16)).pack(pady=10)
    warning = Label(newWindow2, fg="red", text="WARNING: SEEK HELP IF ANY OF THESE SYMPTOMS APPLY TO YOU!", font=("Couier", 16, 'bold')).pack(pady=10)


Button(window, text="Submit", width=10, command=getData).pack(pady=10)

# main function where main back-end code is executed
def main():

    # taking gene input

    # don't make them input in the gene sequence if gene doesn't exist
    # taking gene sequence input
    if gene_exists(gene):
        if mutation_exists(gene, gene_sequence):
            if gene == "hbb":
                SickleCell()
            elif gene == "f8":
                HemophiliaA()
            elif gene == "htt": 
                HuntingtonsDisease()
            else: 
                AlphaThalassemia()
        else:
            label = Label(window, fg="red", text="No Mutation was Found.", font=("Couier", 16)).pack(pady=10)
    else:
        label2 = Label(window, fg="red", text="Gene Does Not Exist in Supported Gene Dictionary. Try (hbb, f8, htt, or hba1).", font=("Couier", 16)).pack(pady=10)


# checks if gene is stored in our gene dictionary
def gene_exists(gene):
    return gene in gene_dict


# checks if there is a mutation in the specific gene and gene sequence entered 
def mutation_exists(gene, gene_sequence):

    # depending on type of possible mutation, refers to specific function
    if gene_dict[gene][1] == "point":
        print("Point check run.")
        return point_check(gene, gene_sequence)
    elif gene_dict[gene][1] == "insertion":
        print("Insertion check run.")
        return insertion_check(gene, gene_sequence)
    else:
        print("Deletion check run.")
        return deletion_check(gene, gene_sequence)

# checks whether gene has a point mutation
def point_check(gene, gene_sequence):

    mutation_start_location = gene_dict[gene][3] - 1
    mutation_code = gene_dict[gene][2]
    mutation_end_location = mutation_start_location+len(mutation_code)
    return gene_sequence[mutation_start_location:mutation_end_location] == mutation_code

# checks whether gene has an insertion mutation
def insertion_check(gene, gene_sequence):

    mutation_range = gene_sequence[gene[3]-1:gene[4]]
    normal_occurrences = gene[5]
    return mutation_range.count(gene[2]) > normal_occurrences

# checks whether gene has a deletion mutation
def deletion_check(gene, gene_sequence):

    total_sequence_count = gene_dict[gene][2]
    deletion_count = gene_dict[gene][3]
    return len(gene_sequence) < total_sequence_count - deletion_count




window.mainloop()
