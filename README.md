# Archive AI

Archive AI is a Python-based vintage clothing management application that allows users to organize, search, edit, and save a digital clothing collection. Version 2 expands the original CRUD application with OpenAI-powered image analysis and resale listing generation.

## Features

- Add clothing manually
- Add clothing using AI image analysis
- Edit and remove clothing items
- Search the closet by clothing attributes
- Save and load closet data using JSON
- Generate marketplace-friendly resale listings using AI
- Review and correct AI-generated clothing information before saving

## AI Image Analysis

Users can provide a local image of a clothing item. Archive AI sends the image to the OpenAI API for analysis and extracts structured clothing information including:

- Brand
- Clothing type
- Estimated year / era
- Style
- Color
- Size
- Condition
- Description

The application uses Pydantic and Structured Outputs to convert the model response into predictable Python data. Users can review and correct the generated information before the item is added to their closet.

## AI Resale Listing Generation

Users can select an existing clothing item and generate a concise, marketplace-friendly resale listing based on its stored attributes.

## Technologies

- Python
- OpenAI API
- OpenAI Python SDK
- Pydantic
- JSON
- Base64 image encoding

## What I Learned

This project began as a way to strengthen my understanding of Python fundamentals, including dictionaries, functions, loops, file I/O, JSON persistence, and CRUD operations.

Version 2 introduced AI application development concepts including API requests and responses, SDKs, authentication with environment variables, model inference, token usage, error handling, multimodal inputs, Base64 image encoding, Pydantic models, and Structured Outputs.

Building the AI features also introduced an important application design principle: AI-generated information should not automatically be treated as correct. Archive AI allows the user to review and modify image-analysis results before they are stored.

## Future Improvements

- Graphical user interface
- File picker for image selection
- Improved clothing image analysis
- Additional resale platform formatting
- More advanced closet filtering and organization

