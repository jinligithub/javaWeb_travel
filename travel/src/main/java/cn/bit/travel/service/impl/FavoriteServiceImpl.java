package cn.bit.travel.service.impl;

import cn.bit.travel.dao.FavoriteDao;
import cn.bit.travel.dao.impl.FavoriteDaoImpl;
import cn.bit.travel.domain.Favorite;
import cn.bit.travel.service.FavoriteService;


public class FavoriteServiceImpl implements  FavoriteService {

    private FavoriteDao favoriteDao = new FavoriteDaoImpl();


    //判断用户是否添加添加收藏
    @Override
    public boolean isFavorite(String rid, int uid) {

        Favorite favorite = favoriteDao.findByRidAndUid(Integer.parseInt(rid), uid);

        return favorite != null;//如果对象有值，则为true，反之，则为false
    }

    //添加收藏
    @Override
    public void add(String rid, int uid) {
        favoriteDao.add(Integer.parseInt(rid),uid);
    }
}
