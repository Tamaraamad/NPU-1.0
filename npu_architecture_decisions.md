
# 🧱 NPU Backend Architecture Decisions

This document outlines the key architectural decisions made during the design and implementation of the NPU Backend system.

---

## 🔐 Security and User Privacy Considerations

1. **Authentication & Authorization**
   - All endpoints are protected using FastAPI dependencies to ensure only authenticated users can access or modify data.
   - Role-based access control is enforced (e.g., superusers can access all data, regular users can only access their own).

2. **Data Ownership**
   - Each NPU creation and score is associated with a `user_id`, ensuring traceability and accountability.

3. **Minimal Exposure**
   - Only necessary fields are exposed via Pydantic schemas (`NPUCreationPublic`, `ScorePublic`).
   - Sensitive fields are excluded from API responses.

4. **Input Validation**
   - Pydantic schemas validate all incoming data to prevent malformed or malicious input.

5. **Static File Security**
   - The `app/static` directory is used for serving static assets and is created with restricted access to prevent directory traversal attacks.

---

## 📈 Scalability and Bottlenecks

1. **Scalability**
   - FastAPI provides asynchronous request handling for high concurrency.
   - SQLModel and SQLAlchemy support efficient database operations.
   - Dockerized architecture allows horizontal scaling using container orchestration tools.

2. **Potential Bottlenecks**
   - **Database Load**: Queries like `search_by_tag` may slow down with large datasets. Indexing or normalization can help.
   - **Image Storage**: If images are stored locally, consider using a CDN or object storage like S3.
   - **Scoring System**: High-frequency writes to the `Score` table may require batching or caching.

3. **Mitigation Strategies**
   - Use pagination for listing endpoints.
   - Add indexes on frequently queried fields (`tags`, `user_id`).
   - Implement rate limiting and caching for public endpoints.

---

## 🧠 Design Principles Applied

1. **Separation of Concerns**
   - Models, schemas, CRUD logic, and routes are modular and isolated.

2. **Modularity**
   - Each feature (e.g., items, NPU) is encapsulated in its own module for easy maintenance and extension.

3. **Reusability**
   - Shared dependencies and schemas are reused across endpoints.

4. **Security by Design**
   - Authentication and authorization are integrated from the start.
   - ORM and schema validation reduce the attack surface.

5. **Scalability Awareness**
   - The system is designed with scalability in mind using FastAPI, Docker, and SQLModel.

---

