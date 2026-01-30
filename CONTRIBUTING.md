
#### 2. 补充`CONTRIBUTING.md`（贡献指南）
```markdown
# 贡献指南
感谢你对OpenDomain AI的关注和贡献！

## 贡献方式
1. 提交Bug反馈（Issue）
2. 提交功能建议（Issue）
3. 提交代码PR（修复Bug/新增功能/完善文档）
4. 完善插件/示例项目

## PR规范
### 分支命名
- 修复Bug：fix/xxx（如fix/wecom-api-retry）
- 新增功能：feat/xxx（如feat/rag-knowledge-base）
- 文档完善：docs/xxx（如docs/deploy-guide）

### 代码规范
- Python代码遵循PEP8规范
- 提交前运行`pytest`确保测试通过
- 新增功能需补充接口文档

## 插件开发规范
1. 插件需继承`core.plugin.base.PluginBase`基类
2. 插件需包含`plugin.json`元数据文件（名称/版本/描述/依赖）
3. 插件代码需包含单元测试

## 审核流程
1. PR提交后，维护者会在2个工作日内审核
2. 审核通过后合并到主分支
3. 重大功能会纳入版本迭代计划
