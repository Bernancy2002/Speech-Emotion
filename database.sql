-- phpMyAdmin SQL Dump
-- version 2.10.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: May 09, 2024 at 11:29 AM
-- Server version: 5.0.45
-- PHP Version: 5.2.5
-- 
-- speech
-- 

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Database: `speechemotion`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `newuser`
-- 

CREATE TABLE `newuser` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

-- 
-- Dumping data for table `newuser`
-- 

INSERT INTO `newuser` (`id`, `name`, `gender`, `email`, `password`) VALUES 
(1, 'kannan', 'male', 'fraudkk123@gmail.com', '1234'),
(2, 'kumar', 'male', '123@gmail.com', '1234');
