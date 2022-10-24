experiments = ['SRP362799', 'ERP126041', 'SRP013555', 'SRP139359', 'SRP212693', 'SRP159219', 'SRP230996', 'SRP363570', 'SRP161571', 'SRP189439']
norm_methods = ['log2_tmm', 'tmm']

del_list = [
    r' \(.*?\)', r' \[.*?\]', r' \{.*?\}',
    'FUNCTION: ', 'TISSUE SPECIFICITY: ', 'INDUCTION: ', 'SUBCELLULAR LOCATION: '
]

colors = ['slategray', '#ffa400', 'crimson']

analysis_tools = {
    'Taxonomy': 'taxonomy', 'Expression values': 'boxplot',
    'eFP': 'eFP', 'Molecule viewer': 'molecule'
}

img_labels = [
    'flower', 'pod', 'vegetative_bud',
    'leaf_with_petiolules', 'petiole', 'stem',
    'mature_nodule', 'nodule_4d', 'nodule_10d', 'nodule_14d',
    'non_inoculated_root', 'root',
    'seed_10d', 'seed_12d', 'seed_16d', 'seed_20d', 'seed_24d', 'seed_36d'
]

color_scale = ['#0053D6', '#65CBF3', '#FFDB13', '#FF7D45']
