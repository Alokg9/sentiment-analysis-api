# sentiment-analysis-api

Sentiment Analysis API – Scalable, Real-Time Sentiment Prediction

![image](https://github.com/user-attachments/assets/95d75b6f-ae10-409a-af6c-8e69d0901471)
![Screenshot 2024-11-13 224007](https://github.com/user-attachments/assets/8f6c0695-0c22-448d-bf18-a0ecade86278)
![Screenshot 2024-11-13 224103](https://github.com/user-attachments/assets/97f8f68b-0247-4da5-914a-26ea71721633)
![Screenshot 2024-11-13 224125](https://github.com/user-attachments/assets/a1392026-0c77-46d1-93e3-0298602ab38a)
![Screenshot 2024-11-13 224140](https://github.com/user-attachments/assets/da1bb70e-53f3-4b8f-b8d8-d0b75924903a)
![Screenshot 2024-11-13 224234](https://github.com/user-attachments/assets/1b8329a3-2d3c-455b-8aad-43d65b4bf83c)
![Screenshot 2024-11-13 224251](https://github.com/user-attachments/assets/1120ab5a-376b-4871-b28f-2d223b40a7d5)
![Screenshot 2024-11-13 224308](https://github.com/user-attachments/assets/29ce53b5-a81f-4239-a648-f49eb4b4e9af)
![Screenshot 2024-11-13 223942](https://github.com/user-attachments/assets/173ab8d7-29ad-45b2-bad4-739cf25f4851)

Objective:
Develop a high-performance Sentiment Analysis API that handles large-scale requests with low latency using FastAPI. The goal was to optimize for speed, accuracy, and scalability by integrating advanced technologies and deploying robust methodologies.

Key Features:
High-Performance API: Built with FastAPI for asynchronous request handling.
ONNX Model Integration: Converted XtremeDistil model with 10M parameters into ONNX for real-time inference.
Quantization & Benchmarking: Reduced model size while maintaining performance.
Gunicorn ASGI Server: Ensures high throughput with concurrent request handling.

Challenges Faced:
Integrating ONNX models while maintaining precision.
Handling high-concurrency environments with FastAPI.
Ensuring robust validation and error handling using Pydantic.

Technical Details:
Model: XtremeDistil trained on the IMDB dataset (25,000 train/test + 50,000 unsupervised data).
ONNX Conversion & Quantization: Enabled faster inference and reduced memory usage.
API Architecture:
FastAPI: Asynchronous, non-blocking request management.
Gunicorn ASGI server: Efficient POST/GET handling for high-volume requests.
Pydantic: Data validation and error handling for clean API operations.

Learning Outcomes:
Concurrency Management: Mastered API scalability using asynchronous programming.
Performance Optimization: Leveraged ONNX and quantization for faster inference.
API Design Principles: Built a resilient API with robust testing and error management.
Real-World Deployment Experience: Optimized API with low-latency benchmarks for production readiness.

