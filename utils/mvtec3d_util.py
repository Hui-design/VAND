import tifffile as tiff
import torch
# from models.pointnet2_utils import interpolating_points


def organized_pc_to_unorganized_pc(organized_pc):
    return organized_pc.reshape(organized_pc.shape[0] * organized_pc.shape[1], organized_pc.shape[2])


def read_tiff_organized_pc(path):
    tiff_img = tiff.imread(path)
    return tiff_img


def resize_organized_pc(organized_pc, img_size=256, tensor_out=True):
    torch_organized_pc = torch.tensor(organized_pc).permute(2, 0, 1).unsqueeze(dim=0).contiguous()
    torch_resized_organized_pc = torch.nn.functional.interpolate(torch_organized_pc, size=img_size,
                                                                 mode='nearest')
    if tensor_out:
        return torch_resized_organized_pc.squeeze(dim=0).contiguous()
    else:
        return torch_resized_organized_pc.squeeze().permute(1, 2, 0).contiguous().numpy()


def organized_pc_to_depth_map(organized_pc):
    return organized_pc[:, :, 2]
