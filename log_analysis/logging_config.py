import logging

def setup_logging():
    """Configure logging for the entire project"""
    
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

def get_logger(name):
    """Get a logger with a specific name for each module"""
    
    return logging.getLogger(name)