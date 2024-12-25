from typing import Tuple

class FileTypes:
    """
        The definition of file classes
    """
    
    VIDEO_EXTENSIONS: Tuple[str, ...] = (
        '.mp4', '.avi', '.mov', '.mkv', 
        '.wmv', '.flv', '.webm', '.m4v', '.3gp'
    )
    
    IMAGE_EXTENSIONS: Tuple[str, ...] = (
        '.jpg', '.jpeg', '.png', '.gif',
        '.webp', '.bmp', '.tiff', '.svg', '.heic'
    )

    @classmethod
    def get_supported_extensions(cls, file_type: str = 'all') -> Tuple[str, ...]:
        """
            Get supported file extensions
        """
        if file_type == 'video':
            return cls.VIDEO_EXTENSIONS
        elif file_type == 'image':
            return cls.IMAGE_EXTENSIONS
        return cls.VIDEO_EXTENSIONS + cls.IMAGE_EXTENSIONS
