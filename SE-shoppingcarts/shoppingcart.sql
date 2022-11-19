-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： localhost:8889
-- 產生時間： 2022 年 11 月 19 日 18:30
-- 伺服器版本： 5.7.34
-- PHP 版本： 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `shoppingcart`
--

-- --------------------------------------------------------

--
-- 資料表結構 `orderlist`
--

CREATE TABLE `orderlist` (
  `id` int(100) NOT NULL,
  `OiD` int(255) NOT NULL,
  `UiD` varchar(10) NOT NULL,
  `PiD` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `orderlist`
--

INSERT INTO `orderlist` (`id`, `OiD`, `UiD`, `PiD`, `amount`, `status`) VALUES
(4, 1, 'user1', 1, 1, 'Shipping/Arrived'),
(5, 1, 'user1', 2, 1, 'Shipping/Arrived'),
(6, 1, 'user1', 4, 1, 'Shipping/Arrived'),
(7, 2, 'user1', 1, 1, 'Preparing'),
(8, 2, 'user1', 2, 1, 'Preparing'),
(9, 2, 'user1', 4, 1, 'Preparing'),
(10, 3, 'user1', 2, 1, 'Preparing'),
(11, 3, 'user1', 4, 1, 'Preparing'),
(12, 3, 'user1', 1, 1, 'Preparing'),
(13, 4, 'user1', 2, 1, 'Preparing'),
(14, 4, 'user1', 4, 1, 'Preparing'),
(15, 4, 'user1', 1, 1, 'Preparing'),
(16, 5, 'user1', 2, 1, 'Shipping/Arrived'),
(17, 5, 'user1', 4, 1, 'Shipping/Arrived'),
(18, 5, 'user1', 1, 1, 'Shipping/Arrived'),
(19, 6, 'user1', 1, 2, 'Shipping/Arrived'),
(20, 6, 'user1', 2, 1, 'Shipping/Arrived'),
(21, 6, 'user1', 4, 3, 'Shipping/Arrived');

-- --------------------------------------------------------

--
-- 資料表結構 `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `Name` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Stock` int(11) NOT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `product`
--

INSERT INTO `product` (`id`, `Name`, `Stock`, `Price`) VALUES
(1, 'Book1', 18, 350),
(2, 'Book2', 19, 500),
(4, 'Book3', 17, 450);

-- --------------------------------------------------------

--
-- 資料表結構 `User`
--

CREATE TABLE `User` (
  `id` varchar(10) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `User`
--

INSERT INTO `User` (`id`, `name`) VALUES
('user1', 'UserA');

-- --------------------------------------------------------

--
-- 資料表結構 `Usercart`
--

CREATE TABLE `Usercart` (
  `id` int(11) NOT NULL,
  `PiD` int(11) NOT NULL,
  `UiD` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `orderlist`
--
ALTER TABLE `orderlist`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `Usercart`
--
ALTER TABLE `Usercart`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `orderlist`
--
ALTER TABLE `orderlist`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `Usercart`
--
ALTER TABLE `Usercart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
