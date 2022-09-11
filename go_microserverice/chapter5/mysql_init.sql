drop table if exists `user`;

create table `user`
(
    `id` int(10) not NULL AUTO_INCREMENT,
    `name` varchar(64) NULL DEFAULT NULL,
    `habits` varchar(128) NULL DEFAULT NULL,
    `created_time` DATE NULL DEFAULT NULL,
    primary key (`id`)
);
