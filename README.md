# Bugzilla Administration Client

A professional, production-grade Python desktop application for administering Bugzilla via REST API.

## Features

- **Modern Qt6 Interface**: Clean, responsive UI with light/dark theme support
- **Complete CRUD Operations**: Users, Groups, Products, Components, Bugs
- **Smart Dependency Handling**: Cascading relationships between entities
- **Interactive Visualizations**: Relationship graphs, dashboard charts, statistics
- **Advanced API Explorer**: Test Bugzilla endpoints with request/response viewer
- **Professional Logging**: Detailed activity logs with export functionality
- **Secure Authentication**: Session-based credential management

## Technology Stack

- **Language**: Python 3.14
- **GUI Framework**: PySide6 (Qt6)
- **API Client**: Requests library
- **Data Processing**: Pandas, OpenPyXL
- **Exports**: CSV, Excel, PDF, JSON

## Project Structure

```
bugzilla_admin/
├── main.py                 # Application entry point
├── config.py               # Configuration management
├── api/                    # Bugzilla REST API layer
├── models/                 # Data models
├── services/               # Business logic
├── ui/                     # User interface
├── resources/              # Assets (icons, stylesheets)
├── utils/                  # Utilities
└── logs/                   # Application logs
```

## Installation

```bash
git clone https://github.com/bccshuvo/bugzilla-admin-client.git
cd bugzilla-admin-client
pip install -r requirements.txt
```

## Running the Application

```bash
python -m bugzilla_admin.main
```

## Development

### Code Quality

- PEP 8 compliant
- Type hints throughout
- Comprehensive docstrings
- Modular architecture

### Testing

```bash
pytest
```

## Features Roadmap

### Phase 1: Core Setup ✓
- Project structure
- Configuration management
- Basic authentication
- API client foundation

### Phase 2: Core Modules (In Progress)
- Users module (CRUD)
- Groups module (CRUD)
- Products module (CRUD)
- Components module (CRUD)
- Bugs module (CRUD)

### Phase 3: Advanced Features
- Relationship Explorer with interactive graphs
- Dashboard charts and statistics
- API Explorer tool
- Bulk operations
- Export functionality (CSV, Excel, PDF)

### Phase 4: Polish & Performance
- Comprehensive logging
- Error handling & recovery
- Performance optimization
- Theme system
- Keyboard shortcuts
- Context menus

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please follow PEP 8 and include tests for new features.
