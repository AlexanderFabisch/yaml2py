import yaml
import yaml2py


yaml_content = """
package: sklearn.pipeline
type: Pipeline
steps:
    - - pca
      - package: sklearn.decomposition
        type: PCA
        n_components: 50
    - - svc
      - package: sklearn.svm
        type: SVC
        gamma: 10.0
"""


if __name__ == "__main__":
    config = yaml.load(yaml_content)
    pipeline = yaml2py.from_dict(config)
    print(pipeline)

    from sklearn.pipeline import Pipeline
    from sklearn.decomposition import PCA
    from sklearn.svm import SVC
    print(Pipeline(steps=[("pca", PCA(n_components=50)),
                          ("svc", SVC(gamma=10.0))]))
