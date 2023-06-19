var express = require('express');
var router = express.Router();

var db = require('../middlewares/db');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  const wantImg = req.query.img;
  const readUser = req.query.frame;

  if(wantImg==='Yes'){
    // 이미지 파일을 읽고 base64로 변환
    const imagePath = 'public/images/sk.png';
    const image = fs.readFileSync(imagePath);
    const base64Image = Buffer.from(image).toString('base64');

    var currentDate = new Date();
    var currentDateTimeString = currentDate.toISOString().slice(0, 19).replace('T', ' ');
    //이메일 열람한 사람
    db.query(`INSERT INTO viewMail ${readUser}, ${currentDateTimeString}`,function(error, results){
      if(error){
        throw error;
      }
    })

    // "Content-Type" 헤더 설정 후 이미지 데이터 전달
    res.set('Content-Type', 'image/png');
    res.send(Buffer.from(base64Image, 'base64'));
  }else{
    //여기선 페이지를 보여주고 싶어
    res.render('index', { title: 'SK' });
  }
});

module.exports = router;