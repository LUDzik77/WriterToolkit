'''

CREATE TABLE `book` (
  `id_book` int NOT NULL DEFAULT '0',
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `completed` tinyint(1) DEFAULT '0',
  `description` mediumtext,
  `narrative` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='id_book 0 is lore, will be added on table generation, not by the user.\nBy default all the content will be added to a book 1ac';


CREATE TABLE `chapter` (
  `id_chapter` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `book` int DEFAULT NULL,
  `book_order` int DEFAULT NULL,
  `lenth_sum` int DEFAULT NULL,
  `completed` tinyint(1) DEFAULT '0',
  `description` mediumtext,
  `narrative` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_chapter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `character` (
  `character_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT 'NOT NULL',
  `family_name` varchar(45) DEFAULT NULL,
  `nickname` varchar(45) DEFAULT NULL,
  `pricipal` tinyint(1) DEFAULT '0',
  `narrative` mediumtext,
  `description` mediumtext,
  `saying` varchar(45) DEFAULT NULL,
  `gender` int DEFAULT '0',
  PRIMARY KEY (`character_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `character_relation` (
  `id_character_relation` int NOT NULL AUTO_INCREMENT,
  `id_character_1` int NOT NULL,
  `id_character_2` int NOT NULL,
  `id_scene` int NOT NULL,
  `type` int NOT NULL,
  `public` tinyint(1) DEFAULT '1',
  `conflict` tinyint(1) DEFAULT '0',
  `description` mediumtext,
  PRIMARY KEY (`id_character_relation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `dictionary` (
  `name` varchar(45) NOT NULL,
  `definition` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `mapping_to_type` (
  `id_mapping_to_type` int NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_mapping_to_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `place` (
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `part_of` varchar(45) DEFAULT NULL,
  `dreamlike` tinyint(1) DEFAULT '0',
  `description` mediumtext,
  `narrative` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `plot` (
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `description` mediumtext,
  `narrative` varchar(45) DEFAULT NULL,
  `herojourney` int DEFAULT NULL,
  `type` int DEFAULT '0',
  `completed` tinyint(1) DEFAULT '0',
  `principal` tinyint(1) DEFAULT '0',
  `sideplot` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `plot_scene_relation` (
  `plot_name` varchar(45) NOT NULL,
  `scene name` varchar(45) NOT NULL,
  `plot_type` int DEFAULT NULL,
  PRIMARY KEY (`plot_name`,`scene name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `scene` (
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `description` mediumtext,
  `location` varchar(45) DEFAULT NULL,
  `principal` tinyint(1) DEFAULT '0',
  `cliffhanger` tinyint(1) DEFAULT '0',
  `drama_level` int DEFAULT '2',
  `chapter` int DEFAULT NULL,
  `chapter_order` int DEFAULT NULL,
  `length` int DEFAULT NULL,
  `completed` tinyint(1) DEFAULT '0',
  `narrative` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `scene_member` (
  `scene_name` varchar(45) NOT NULL,
  `character_id` int NOT NULL,
  PRIMARY KEY (`scene_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `team` (
  `name` varchar(45) NOT NULL DEFAULT 'UNIQUE',
  `description` mediumtext,
  `narrative` varchar(45) DEFAULT NULL,
  `nr_members` int DEFAULT '0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `team_member_scene` (
  `team_name` varchar(45) NOT NULL,
  `character_id` int NOT NULL,
  `scene_name` int NOT NULL,
  `type` int DEFAULT NULL,
  `public` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`team_name`,`character_id`,`scene_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


'''