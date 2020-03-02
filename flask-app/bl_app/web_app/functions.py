

def disease_filter(disease):
    """
        This takes in the string of a disease name as an argument, and returns
        the dosage, schedule, and intake method corresponding to that disease.

        Returns "Invalid Disease Entry" if disease name is not found.
    """
    disease_dict = {
    'Cancer - Pain': 'Daily Dosage: 17mg THC or 16mg CBD, in 6 sprays spread out over a 24-hour period.',
    'Cancer - Nausea': 'Daily Dosage: 10-18mg THC. Take a capsule 1 hr prior to chemo, then every 2-4 hrs over 12-24 hrs.',
    'Cancer - Wasting':	'Daily Dosage: 10-15mg THC. Take plant-derived medication 3-4 times daily on chemo days.',
    'Glaucoma':	'Daily Dosage: 5mg THC. Take 1 capsule.',
    'HIV/AIDS': 'Daily Dosage: 5-7mg THC. Take 2-3 capsules.',
    'Seizures':	'Daily Dosage: 2-5mg CBD. Take 1 dose of oral solution, and increase dosage over 2-4 weeks.',
    'Muscle Spasms': 'Daily Dosage: 20-25mg THC. Divide doses (in capsule form) over the day.',
    'Autism': 'Daily Dosage: 2.5mg-10mg CBD. Start with low dose of oral solution, and increase over time.',
    'Sleep Apnia': 'Daily Dosage: 2.5-10mg THC.	Take 1 capsule at bedtime.',
    'Tourette Syndrome': 'Daily Dosage: 2.5-10mg THC. Take 1 capsule.',
    'ALS': 'Daily Dosage: 2.5-10mg THC.	Take 1 capsule, and increase dosage over time.',
    'IBS': 'Daily Dosage: 5mg CBD. Use 2 extracts per day, place under tongue.',
    'Intractable Pain':	'Daily Dosage: 15-27mg THC/CBD. Spray 6-10 times per day.',
    'PTSD':	'Daily Dosage: 5mg THC.	Take 2 oral solutions, place under tongue.'
    }

    return disease_dict.get(disease, 'Invalid Disease Entry')
