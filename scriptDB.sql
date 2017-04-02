create database testdb; 
use testdb;

CREATE TABLE IF NOT EXISTS car_Data (

	id int not null AUTO_INCREMENT PRIMARY KEY,
	title text,
    hourData text,
    ubication text,
    price double,
    anno int,
    usageData text,
    km int,
    gas text,
    trans text,
    model text,
    color text,
    description text,
    seller text,
    phone int,
    image text
    
) ENGINE=InnoDB;

delimiter $$
create procedure sp_insert_Car_Data(
	in _title text,
    in _hourData text,
    in _ubication text,
    in _price double,
    in _anno int,
    in _usageData text,
    in _km int,
    in _gas text,
    in _trans text,
    in _model text,
    in _color text,
    in _description text,
    in _seller text,
    in _phone int,
    in _image text
    
) 
begin
	insert into car_Data (title, hourData, ubication, price, anno, usageData, km, gas, trans, model, color, description, seller, phone, image)
    values (_title, _hourData, _ubication, _price, _anno, _usageData, _km, _gas, _trans, _model, _color, _description, _seller, _phone, _image);
end $$
delimiter ;
