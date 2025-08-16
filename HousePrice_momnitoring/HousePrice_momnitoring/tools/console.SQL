create database HousePrice charset'utf8';


use HousePrice;

create table if not exists ershoufang(
    id int primary key auto_increment,
    houseID varchar(30) unique,           -- 房子id
    platformID varchar(30),               -- 平台
    province varchar(30),                 -- 省
    city varchar(30),                     -- 市
    district VARCHAR(50),                 -- 区或县
    price DECIMAL(10,2),                   -- 总价（万元）
    unit_price DECIMAL(10,2),              -- 单价（元/㎡）
    area DECIMAL(10,2),                    -- 面积（㎡）
    house_type VARCHAR(50),                -- 户型
    floor VARCHAR(50),                     -- 楼层
    orientation VARCHAR(50),               -- 朝向
    year_built VARCHAR(20),                -- 建造年份  链家没有
    community varchar(50),                 -- 小区名
    title VARCHAR(255),                   -- 房源标题
    source_url TEXT,                       -- 房源链接
    crawl_time DATETIME                    -- 爬取时间

);

drop table ershoufang;
desc ershoufang;


select * from ershoufang;
