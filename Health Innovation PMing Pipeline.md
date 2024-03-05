Simulating Educational Stories using GenAI. E.g. Train Med Students on LLMs.

### ChatGPT Prompt Used :

https://chat.openai.com/g/g-HMNcP6w7d-data-analyst/c/a7228dc8-744a-446b-be88-84cfbc8997d7

Data Source : https://ucdavis365.sharepoint.com/:x:/r/sites/AIFHIRServer/Shared%20Documents/AI%20Sandbox%20v1.0/1.%20Project%20Initiation%20%26%20Planning/DD_AI_Sandbox_Beta_User_Survey_March_4,_2024_13.04%5B1%5D.xlsx?d=wdeeebfa3e33d4967adcf2416247552f8&csf=1&web=1&e=PdhXpY

![alt text](image.png)

##### INPUT :

Information Provided :

To fetch the details of Dr. JP Graff from the file you've uploaded earlier, I'll go back to the data extracted from the Excel file and provide you with a summary of his details based on the information available in that dataset. Let's review the information related to Dr. JP Graff from the provided file.

Based on the earlier analysis of the file content, here are the details related to Dr. JP Graff:

### Doctor Name:

- **JP Graff**

### Designation:

- **Associate Prof**

### Department:

- **Pathology**

### Questions and Answers:

1. **Q3: Implementation challenges and scaling of ML models**

   - **Response:** "implementation challenges and scaling of ML models in pathology"

2. **Q4: Interest in AI/ML Applications**

   - **Response:** "object detection on whole slide imaging (SVS files) using openslide API linked to python or similar setups"

3. **Q5: Data Types and Formats for AI/ML Applications**

   - **Response:** "WSI files using either openslide API linked to python or similar setups"

4. **Q6: Support and Collaboration Needs**

   - **Response:** "linux kernal and command line coders to aid in data processing and model implementation"

5. **Q7_1 to Q7_26: Previous Utilization of AI/ML Tools (Selected Responses)**

   - **Responses:** Indicated previous use of AI/ML tools, specifically mentioned were "Previously Used" for several categories.

6. **Q8: Other AI/ML Tools Mentioned**

   - **Response:** "IBM PowerAI, Microsoft Power automate, and NVIDIA Clara"

7. **Q9: AI-powered digital health technologies**

   - **Response:** "WSI analysis using CNNs"

8. **Q10: Willingness to Dedicate Time**
   - **Response:** Indicated a willingness to dedicate "10" hours.

This summary encapsulates the key details provided by Dr. JP Graff in the survey, reflecting his interests and experiences with AI/ML in the field of pathology. If you need more detailed information or have specific questions, please let me know!

#### Output :

Analysis Sheet :

https://ucdavis365.sharepoint.com/:x:/r/sites/AIFHIRServer/Shared%20Documents/AI%20Sandbox%20v1.0/1.%20Project%20Initiation%20%26%20Planning/User%20Survey%20Response%20Analysis.xlsx?d=w6a56c62af72447ecabeabae4dfb17ea4&csf=1&web=1&e=5x8bbT

![alt text](image-1.png)

### How do we automate This ?

For ValidAI & Digital Davis AI Sandbox : Partnership with Microsoft and Epic AI Sandbox https://www.youtube.com/watch?v=R8YR243hbNA

what ? Voice to Epic :

![alt text](image-10.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)

For UCDH-IT Internal Use :
Partnership with ServiceNow and NVIDIA
https://www.youtube.com/watch?v=XqbXLxqZGhY&t=237s

![alt text](image-4.png)
![alt text](image-5.png)

#### Output PMing:

Google : Thank you for providing a 100000 Tokens window.

https://gemini.google.com/app/2f96156cb3acd65b

![alt text](image-2.png)

</ Example Answer Start >

**Context Aware Token Pipeline**

This section outlines how to convert the provided data types into context-aware tokens with start and end markers.

**Example:**

- `ProjectID: str` translates to: `< ProjectID Start >` ... `< ProjectID End >`

**Tokenization Rules:**

1. Each data type definition is encapsulated within its own start and end tokens.
2. Use a descriptive naming convention for tokens, reflecting the data type (e.g., `< ProjectName Start >`, `< DataSize End >`).
3. Consider using a consistent delimiter (e.g., `>`) to separate start and end tokens.

**Applying the Rules:**

Here's the complete list of data types converted into context-aware tokens:

- `< ProjectID Start >` ... `< ProjectID End >` (str)
- `< ProjectName Start >` ... `< ProjectName End >` (str)
- `< ProjectDescription Start >` ... `< ProjectDescription End >` (str)
- `< StartDate Start >` ... `< StartDate End >` (datetime.date)
- `< EndDate Start >` ... `< EndDate End >` (datetime.date)
- `< ProjectStatus Start >` ... `< ProjectStatus End >` (Enum("In Progress", "Completed", "On Hold"))
- `< TeamMembers Start >` ... `< TeamMembers End >` (List[str])

- `< DatasetID Start >` ... `< DatasetID End >` (str)
- `< DatasetName Start >` ... `< DatasetName End >` (str)
- `< DataType Start >` ... `< DataType End >` (Enum("Image", "Text", "Tabular"))
- `< DataFormat Start >` ... `< DataFormat End >` (str)
- `< DataLocation Start >` ... `< DataLocation End >` (str)
- `< DataSize Start >` ... `< DataSize End >` (int)

- `< ModelID Start >` ... `< ModelID End >` (str)
- `< ModelName Start >` ... `< ModelName End >` (str)
- `< ModelType Start >` ... `< ModelType End >` (Enum("Classification", "Regression", "Clustering"))
- `< ModelArchitecture Start >` ... `< ModelArchitecture End >` (str)
- `< TrainingParameters Start >` ... `< TrainingParameters End >` (Dict[str, Any])
- `< PerformanceMetrics Start >` ... `< PerformanceMetrics End >` (Dict[str, float])

</ Example Answer End >

This approach provides a clear and structured method for converting data types into context-aware tokens within your AI Project Management system.
