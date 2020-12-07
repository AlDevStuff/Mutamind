
'''
    ONLY BACKEND OF THE SOFTWARE
'''

# # # importing regular expressions
# # import re

# # # regular expression to detect any digits or spaces (in order to isolate just the letters)
# # gene_regex = re.compile(r"\d| ")

# # """
# # dictionary documenting each supported mutation 
# # * key = gene name (because the user will input the gene name) 
# # * value = list containing various properties of the specific mutation related to the key
# #     - each property explained ahead 
# # """
# # gene_dict = {
# #     # gene: [mutation name, point mutation, letter at point mutation, index of point mutation (starting with 1)]
# #     "hbb": ["Sickle-cell Anemia", "point", "t", 65],

# #     # gene: [mutation name, point mutation, letter at point mutation, index of point mutation (starting with 1)]
# #     "f8": ["Hemophilia A", "point", "a", 191799],

# #     # gene: [mutation name, insertion mutation, sequence inserted, index where exon starts, index where exon finishes,
# #     # normal number of "cag" sequences]
# #     "htt": ["Huntington's Disease", "insertion", "cag", 5001, 5414, 28],

# #     # gene: [mutation name, deletion mutation, normal number of characters in gene sequence, length of exon omitted]
# #     "hba1": ["Alpha Thalassemia", "deletion", 7872, 830]
# # }


# # main function where all code is executed
# def main():

#     # taking gene input
#     gene = input("Type the gene: ").lower()

#     # don't make them input in the gene sequence if gene doesn't exist
#     # taking gene sequence input
#     gene_sequence = input("Type the gene sequence (you might want to just copy and paste this one): ").lower()
#     gene_sequence = re.sub(gene_regex, "", gene_sequence)
#     print(gene_sequence)
#     if gene_exists(gene):
#         if mutation_exists(gene, gene_sequence):
#             print(gene_dict[gene])
#         else:
#             print("Mutation not found.")
#     else:
#         print("Gene not in dictionary.")


# def gene_exists(gene):
#     return gene in gene_dict


# def mutation_exists(gene, gene_sequence):

#     # depending on type of mutation, refer to specific function
#     if gene_dict[gene][1] == "point":
#         print("Point check run.")
#         return point_check(gene, gene_sequence)
#     elif gene_dict[gene][1] == "insertion":
#         print("Insertion check run.")
#         return insertion_check(gene, gene_sequence)
#     else:
#         print("Deletion check run.")
#         return deletion_check(gene, gene_sequence)


# def point_check(gene, gene_sequence):

#     mutation_start_location = gene_dict[gene][3] - 1
#     mutation_code = gene_dict[gene][2]
#     mutation_end_location = mutation_start_location+len(mutation_code)
#     return gene_sequence[mutation_start_location:mutation_end_location] == mutation_code


# def insertion_check(gene, gene_sequence):

#     mutation_range = gene_sequence[gene[3]-1:gene[4]]
#     normal_occurrences = gene[5]
#     return mutation_range.count(gene[2]) > normal_occurrences


# def deletion_check(gene, gene_sequence):

#     total_sequence_count = gene_dict[gene][2]
#     deletion_count = gene_dict[gene][3]
#     return len(gene_sequence) < total_sequence_count - deletion_count


# # calling main function
# main()































