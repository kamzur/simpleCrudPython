-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2014 at 05:52 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `mhs`
--

CREATE TABLE IF NOT EXISTS `mhs` (
  `nim` varchar(15) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `email` varchar(70) NOT NULL,
  `jurusan` varchar(40) NOT NULL,
  PRIMARY KEY (`nim`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mhs`
--

INSERT INTO `mhs` (`nim`, `nama`, `email`, `jurusan`) VALUES
('1111503007', 'Yanwar', 'yanzen@gmail.com', 'Teknik Informatika'),
('1234567', 'Yuan', 'yuanwei@yahoo.com', 'Teknik Pertambangan'),
('1345690', 'Jani Sulaiman', 'solomon@gmail.com', 'Kehutanan'),
('167865', 'solahudin', 'solahudin@gmail.com', 'Teknologi Listrik'),
('16786523', 'solahudins', 'solahudin@gmail.com', 'Teknologi Listrik'),
('34567', 'Jani', 'jajani@yahoo.com', 'Teknik Perkapalan'),
('dasd', 'dsadas', 'adasdasd', 'asdas');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
