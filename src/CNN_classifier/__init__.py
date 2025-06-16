import os
import logging
import sys

log_dir = "logs"

os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, "cnn_classifier.log")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_filepath)])

logger = logging.getLogger("CNN-classifierLogger")    

