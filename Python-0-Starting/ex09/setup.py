from setuptools import setup, find_packages

setup(
    name="ft_package",  # Paketinizin adı (pip show'daki Name)
    version="0.0.1",  # Sürüm numarası (pip show'daki Version)
    packages=find_packages(),  # Paketleri otomatik bulmak için
    include_package_data=True,  # README.md, LICENSE gibi dosyaları dahil etmek için
    install_requires=[],  # Bağımlılıklar varsa buraya eklenir
    description="A sample test package",  # Kısa açıklama (pip show'daki Summary)
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # PyPI'de README.md'yi Markdown olarak göstermek için
    author="eagle",  # Yazar adı (pip show'daki Author)
    author_email="eagle@42.fr",  # Yazar e-posta adresi (pip show'daki Author-email)
    url="https://github.com/eagle/ft_package",  # Proje URL'si (pip show'daki Home-page)
    python_requires='>=3.6',  
    license="MIT",  # Lisans türü (pip show'daki License)
)
