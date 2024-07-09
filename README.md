# MCQ GENERATOR

## Overview

The MCQ Generator is a Python project that automates the process of generating multiple-choice questions (MCQs) for educational purposes. It utilizes Generative AI technologies like Langchains to analyze input text and create relevant MCQs based on the given number of questions, level of difficulty, and the subject.

Live app - [Click here](https://mcqs-generator.streamlit.app)

![MCQ Image](https://imgs.search.brave.com/nSpZtY-jGvSVnq_koyNnFfCOOD7HS_R2F04SeshN5RU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQ2/MDczODU3OS9waG90/by9idXNpbmVzc21h/bi10aWNrLW1hcmst/YW4tYXNzZXNzbWVu/dC1xdWVzdGlvbm5h/aXJlLWV2YWx1YXRp/b24tb25saW5lLXN1/cnZleS1vbmxpbmUt/ZXhhbS53ZWJwP2I9/MSZzPTE3MDY2N2Em/dz0wJms9MjAmYz1Z/RVY0ZmVEQ2ZWUk05/NG9KU2NnQkp5Sllm/Y2ZFQ2g3M3VYcVVU/UVB6dzljPQ)

## Installation

To install the MCQ Generator, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/mcq-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mcq-generator
   ```

3. Install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables:
   - Signin to AI21 studio, generate your API KEY and copy it, create a `.env` file and add an evironemnt variable like following in the .env file.
     ```bash
     AI21_API_KEY = "your_key"
     ```

2. Run the Streamlit Application:
   ```bash
   streamlit run streamlitApp.py
   ```

3. Follow the prompts to input the text, specify the number of questions, and customize other parameters as needed.

4. Review the generated MCQs and make any necessary adjustments to the prompts in the `MCQGenerator.py` file accordingly.

## Contributing

Contributions to the MCQ Generator project are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## Contact

For any inquiries or feedback, please contact [sansyprog8@gmail.com](mailto:sansyprog8@gmail.com).

Feel free to customize and expand upon this template to suit your project's specific needs!
