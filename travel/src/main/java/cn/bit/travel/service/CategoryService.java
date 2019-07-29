package cn.bit.travel.service;

import cn.bit.travel.domain.Category;

import java.util.List;

public interface CategoryService {
    //查找所有的种类
    public List<Category> findAll();
}
