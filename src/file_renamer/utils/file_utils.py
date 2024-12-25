from typing import Tuple

class FileTypes:
    """
        The definition and process of file classes
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
            Args:
                file_type: Type of files ('all', 'video', 'image')
            Returns:
                The tuple of supported extensions of files
        """
        if file_type not in ('all', 'video', 'image'):
            raise ValueError(f"Unsupported file type: {file_type}")

        if file_type == 'video':
            return cls.VIDEO_EXTENSIONS
        elif file_type == 'image':
            return cls.IMAGE_EXTENSIONS
        return cls.VIDEO_EXTENSIONS + cls.IMAGE_EXTENSIONS
