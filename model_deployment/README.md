# Model deployment

Run the API with:

```python
python -m uvicorn main:app --reload
```

Send an example request with:

http://127.0.0.1:8000/docs#/

First modify request URLs on `app.py` to `<127.0.0.1:8000>`, then run dashboard with:

```python
python app.py
```

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](LICENSE)**
- Copyright 2023 © Felix Rojas, Daniel Reales & Juan Alegría
