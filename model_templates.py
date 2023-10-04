diagnosis_report_template = """Based on the conversation transcript and the pharmacist's hints provided below, generate a detailed diagnosis note in the following format:
Diagnosis:
History of Presenting Illness:
Medications (Prescribed): List current medications and note if they are being continued, or if any new ones have been added.
Diagnosis Report:
Symptom statement: List the symptoms mentioned in the transcript
Diagnosis: 
History of Presenting Illness:
Initial treatment: 
Medications (Prescribed): List current medications and note if they are being continued, or if any new ones have been added.
Specific Advice for the Patient: List some specific advice related to their diagnosis and diet to the patient

Please consider any information in the transcript that might be relevant to each of these sections, and use the pharmacist's hint as a guide.

### Example
Conversation Transcript:
Pharmacist (Ph): “Good day ma, what is troubling you?”
Patient (Pt): “I have headache, soar throat and cough. I've been taking Panadol for 4 days now as another pharmacist prescribed, but I'm still feeling quite unwell.”
Ph: “How old are you?”
Pt: “I am 33.”
Ph: Any recent health issues or surgeries?
Pt: No, I'm generally healthy.
Ph: Describe your headache.
Pt: It's a throbbing pain around my eyes.
Ph: Sore throat and cough duration?
Pt: Sore throat for three days, cough for two.
Ph: Fever or chills?
Pt: No fever, but I feel chilled sometimes.


Diagnosis Report:

Symptom statement: The symptoms mentioned by the patient are a headache, sore throat, and cough

Diagnosis: Mild respiratory infection

History of Presenting Illness: The patient has been using panadol but there seems to be no change

Initial treatment: 
- Panadol
Medications (Prescribed):
[Continue] Panadol
[Added] Acetaminophen (e.g., Tylenol) or ibuprofen (e.g., Advil, Motrin) | Pain and Fever Relievers:
   - These over-the-counter (OTC) medications can help reduce fever and alleviate aches and pains associated with respiratory infections.
[Added] Pseudoephedrine (e.g., Sudafed) or phenylephrine (e.g., Sudafed PE) | Decongestants:
   - Decongestants can provide temporary relief from nasal congestion, but they should be used cautiously and for a short duration.
[Added] Loratadine (e.g., Claritin) or cetirizine (e.g., Zyrtec) | Antihistamines:
   - Antihistamines may help with symptoms like sneezing and runny nose, particularly if allergies contribute to your symptoms.

Specific Advice for the Patient:
- Do not give the child sugary drinks, herbal tea, or coffee.
- Food should be processed and mashed. Maintain regular daily meals: encourage eating more if the child wants to, and eat frequently in small amounts, with meals spaced 3-4 hours apart (6 meals a day). Avoid diluting food. Avoid too many fibrous fruits and vegetables and foods with excessive sugar.
- Seek medical attention if there are symptoms: continuous watery stools, recurring vomiting, excessive thirst, poor appetite, refusing to eat or breastfeed, no improvement after 2 days of treatment, high fever, blood in stool.

Now, based on the following conversation and hints, please generate a diagnosis report:

### Conversation Transcript
{transcript}

### Pharmacist's Hint
{pharmacist_hint}
"""


### This template is for the differential diagnosis and possible questions the pharmacist can ask
diffdiag_and_questions_template = """Based on the provided transcript snippets from a pharmacist-patient consultation, please parse the information and generate a differential diagnosis, as well as potential questions the pharmacist could ask to facilitate the diagnosis process. The results should be organized in the following format:
Differential Diagnosis: List each possible diagnosis with a model confidence score from 0%-100%, 100% being most confident.
Questions to Ask: Provide a list of relevant questions the pharmacist could ask to further clarify the diagnosis.
Please consider the patient's stated symptoms, age, their medical history, and any other relevant information presented in the transcript. The consultation snippets are as follows:

{transcript}
"""

### This template is for the differential diagnosis
diffdiag_template = """##DDX model
Based on the provided transcript snippets from a pharmacist-patient consultation, parse the information to generate a differential diagnosis. The results should be organized as follows:
Differential Diagnosis: List each possible diagnosis with a model confidence score from 0%-100% (example: [30%]), 100% being most confident.
Please consider the patient's stated symptoms, age, their medical history, and any other relevant information presented in the transcript. The consultation snippets are as follows:

{transcript}
Differential Diagnosis:
"""

### This template is for the possible questions the pharmacist can ask
questions_template = """##Pharmacist QA model
Based on the provided transcript snippets from a pharmacist-patient consultation, internally generate a differential diagnosis based on the patient's stated symptoms, their medical history, and any other relevant information presented in the transcript. Then, suggest potential questions the pharmacist could ask to facilitate the diagnosis process. The questions should be aimed at clarifying the diagnosis or gathering more information to refine the differential diagnosis.
The differential diagnosis should not be output. The results should be formatted as follows:
Questions to Ask: Provide a list of top 3 relevant questions the pharmacist could ask to further clarify the diagnosis. The question is succint and short.
The consultation snippets are as follows:

{transcript}
Questions to Ask:
"""