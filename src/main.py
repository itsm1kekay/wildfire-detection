import zarr
import fsspec
import xarray as xr


url = 'https://storage.de.cloud.ovh.net/v1/AUTH_84d6da8e37fe4bb5aea18902da8c1170/uc3/uc3cube.zarr'
ds = xr.open_zarr(fsspec.get_mapper(url), consolidated=True)
print(ds.head())
