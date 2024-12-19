from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

class MenuItem(BaseModel):
    id: int
    name: str
    description: str

class Service(BaseModel):
    id: int
    name: str
    description: str

class Contact(BaseModel):
    address: str
    phone: str
    email: str

MENU_DB = [
    MenuItem(id=1, name="Эспрессо", description="Классический итальянский эспрессо, приготовленный из свежеобжаренных зерен."),
    MenuItem(id=2, name="Капучино", description="Нежный и кремовый капучино с молочной пенкой."),
    MenuItem(id=3, name="Латте", description="Мягкий и сливочный латте с различными ароматизаторами."),
    MenuItem(id=4, name="Американо", description="Легкий и освежающий американо для тех, кто предпочитает менее крепкий кофе."),
    MenuItem(id=5, name="Мокко", description="Сладкий и насыщенный мокко с добавлением шоколада."),
    MenuItem(id=6, name="Черный чай", description="Классический черный чай различных сортов."),
    MenuItem(id=7, name="Зеленый чай", description="Оздоравливающий зеленый чай с различными добавками."),
    MenuItem(id=8, name="Травяные чаи", description="Разнообразие травяных чаев для улучшения настроения и здоровья."),
    MenuItem(id=9, name="Чизкейки", description="Разнообразные чизкейки с различными начинками."),
    MenuItem(id=10, name="Макароны", description="Французские макароны различных вкусов."),
    MenuItem(id=11, name="Тирамису", description="Классический итальянский десерт с кофе и маскарпоне."),
    MenuItem(id=12, name="Шоколадные пирожные", description="Мягкие и воздушные шоколадные пирожные."),
    MenuItem(id=13, name="Сэндвичи", description="Свежие сэндвичи с различными начинками."),
    MenuItem(id=14, name="Салаты", description="Легкие и полезные салаты."),
    MenuItem(id=15, name="Супы", description="Домашние супы для тех, кто хочет перекусить чем-то теплым и сытным."),
]

SERVICES_DB = [
    Service(id=1, name="Бесплатный Wi-Fi", description="Кафе 'По кофейку?' предоставляет бесплатный доступ к Wi-Fi для всех посетителей."),
    Service(id=2, name="Коворкинг-зона", description="Удобное место для работы или учебы с розетками и тихой обстановкой."),
    Service(id=3, name="Проведение мероприятий", description="Возможность проведения встреч, мастер-классов и праздников."),
    Service(id=4, name="Доставка", description="Доставка любимых напитков и блюд прямо к вашему дому или офису."),
    Service(id=5, name="Лояльная программа", description="Накопление баллов за каждый визит и получение скидок и бонусов."),
]

CONTACT_DB = Contact(
    address="ул. Профсоюзов, 8, г. Сургут",
    phone="8(945) 426-89-27",
    email="info@pokofeyku.com"
)

app = FastAPI()

@app.get("/menu/")
def read_menu():
    return MENU_DB

@app.get("/menu/{id}")
def read_menu_item(id: int):
    for item in MENU_DB:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Пункт меню не найден")

@app.post("/menu/")
def create_menu_item(item: MenuItem):
    for existing_item in MENU_DB:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Пункт меню с таким ID уже существует")
    MENU_DB.append(item)
    return item

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for index, item in enumerate(MENU_DB):
        if item.id == id:
            del MENU_DB[index]
            return {"message": "Пункт меню успешно удален"}
    raise HTTPException(status_code=404, detail="Пункт меню не найден")

@app.get("/services/")
def read_services():
    return SERVICES_DB

@app.get("/services/{id}")
def read_service(id: int):
    for service in SERVICES_DB:
        if service.id == id:
            return service
    raise HTTPException(status_code=404, detail="Услуга не найдена")

@app.get("/contact/")
def read_contact():
    return CONTACT_DB

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
