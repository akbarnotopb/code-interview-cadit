-- homestead.Genre definition

CREATE TABLE `Genre` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


-- homestead.Movies definition

CREATE TABLE `Movies` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `plot` text,
  `rating` float DEFAULT NULL,
  `duration` int(10) unsigned DEFAULT NULL,
  `votes` int(10) unsigned DEFAULT NULL,
  `revenue` double DEFAULT NULL,
  `release_detail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- homestead.Stars definition

CREATE TABLE `Stars` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


-- homestead.MoviesGenre definition

CREATE TABLE `MoviesGenre` (
  `id_movies` bigint(20) unsigned NOT NULL,
  `id_genre` bigint(20) unsigned NOT NULL,
  KEY `MoviesGenre_Movies_FK` (`id_movies`),
  KEY `MoviesGenre_Genre_FK` (`id_genre`),
  CONSTRAINT `MoviesGenre_Genre_FK` FOREIGN KEY (`id_genre`) REFERENCES `Genre` (`id`) ON DELETE CASCADE,
  CONSTRAINT `MoviesGenre_Movies_FK` FOREIGN KEY (`id_movies`) REFERENCES `Movies` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- homestead.Roles definition

CREATE TABLE `Roles` (
  `id_movies` bigint(20) unsigned NOT NULL,
  `id_roles` bigint(20) unsigned NOT NULL,
  `sebagai` enum('Director','Star') NOT NULL,
  KEY `Roles_Movies_FK` (`id_movies`),
  KEY `Roles_Stars_FK` (`id_roles`),
  CONSTRAINT `Roles_Movies_FK` FOREIGN KEY (`id_movies`) REFERENCES `Movies` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Roles_Stars_FK` FOREIGN KEY (`id_roles`) REFERENCES `Stars` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;