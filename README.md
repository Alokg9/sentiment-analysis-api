# sentiment-analysis-api

Sentiment Analysis API – Scalable, Real-Time Sentiment Prediction

![image](https://github.com/user-attachments/assets/95d75b6f-ae10-409a-af6c-8e69d0901471)
![Screenshot 2024-11-13 224308](https://github.com/user-attachments/assets/f2aaecd0-ba68-42cc-9e9e-d001fcb3a555)


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

