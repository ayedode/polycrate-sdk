from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_icon_upload_create_active_error_component import (
        ApiV1ProvidersIconUploadCreateActiveErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_address_error_component import (
        ApiV1ProvidersIconUploadCreateAddressErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_annotations_error_component import (
        ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_archived_at_error_component import (
        ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_archived_error_component import (
        ApiV1ProvidersIconUploadCreateArchivedErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_archived_reason_error_component import (
        ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_asn_error_component import (
        ApiV1ProvidersIconUploadCreateAsnErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_ccm_block_error_component import (
        ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_certifications_error_component import (
        ApiV1ProvidersIconUploadCreateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_criticality_error_component import (
        ApiV1ProvidersIconUploadCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_csi_controller_block_error_component import (
        ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_csi_storage_classes_error_component import (
        ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_debug_mode_error_component import (
        ApiV1ProvidersIconUploadCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_display_name_error_component import (
        ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_emails_error_component import (
        ApiV1ProvidersIconUploadCreateEmailsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_icon_content_type_error_component import (
        ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_icon_filename_error_component import (
        ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_kind_error_component import (
        ApiV1ProvidersIconUploadCreateKindErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_labels_error_component import (
        ApiV1ProvidersIconUploadCreateLabelsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_legal_name_error_component import (
        ApiV1ProvidersIconUploadCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_name_error_component import (
        ApiV1ProvidersIconUploadCreateNameErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_non_field_errors_error_component import (
        ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_phone_error_component import (
        ApiV1ProvidersIconUploadCreatePhoneErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_platform_service_error_component import (
        ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_provider_error_component import (
        ApiV1ProvidersIconUploadCreateProviderErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_provider_id_error_component import (
        ApiV1ProvidersIconUploadCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_provider_reference_error_component import (
        ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_reconciliation_enabled_error_component import (
        ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_sla_availability_error_component import (
        ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_sla_target_error_component import (
        ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_slo_availability_error_component import (
        ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_slo_target_error_component import (
        ApiV1ProvidersIconUploadCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_slug_error_component import (
        ApiV1ProvidersIconUploadCreateSlugErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_target_availability_error_component import (
        ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_tolerations_error_component import (
        ApiV1ProvidersIconUploadCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_icon_upload_create_urls_error_component import (
        ApiV1ProvidersIconUploadCreateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProvidersIconUploadCreateValidationError")


@_attrs_define
class ApiV1ProvidersIconUploadCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersIconUploadCreateActiveErrorComponent |
            ApiV1ProvidersIconUploadCreateAddressErrorComponent | ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent |
            ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent | ApiV1ProvidersIconUploadCreateArchivedErrorComponent |
            ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent | ApiV1ProvidersIconUploadCreateAsnErrorComponent |
            ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent |
            ApiV1ProvidersIconUploadCreateCertificationsErrorComponent |
            ApiV1ProvidersIconUploadCreateCriticalityErrorComponent |
            ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent |
            ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent |
            ApiV1ProvidersIconUploadCreateDebugModeErrorComponent | ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent
            | ApiV1ProvidersIconUploadCreateEmailsErrorComponent |
            ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent |
            ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent | ApiV1ProvidersIconUploadCreateKindErrorComponent |
            ApiV1ProvidersIconUploadCreateLabelsErrorComponent | ApiV1ProvidersIconUploadCreateLegalNameErrorComponent |
            ApiV1ProvidersIconUploadCreateNameErrorComponent | ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent |
            ApiV1ProvidersIconUploadCreatePhoneErrorComponent | ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent
            | ApiV1ProvidersIconUploadCreateProviderErrorComponent | ApiV1ProvidersIconUploadCreateProviderIdErrorComponent
            | ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent |
            ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent |
            ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent |
            ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent |
            ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent |
            ApiV1ProvidersIconUploadCreateSloTargetErrorComponent | ApiV1ProvidersIconUploadCreateSlugErrorComponent |
            ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent |
            ApiV1ProvidersIconUploadCreateTolerationsErrorComponent | ApiV1ProvidersIconUploadCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersIconUploadCreateActiveErrorComponent
        | ApiV1ProvidersIconUploadCreateAddressErrorComponent
        | ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent
        | ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent
        | ApiV1ProvidersIconUploadCreateArchivedErrorComponent
        | ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent
        | ApiV1ProvidersIconUploadCreateAsnErrorComponent
        | ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent
        | ApiV1ProvidersIconUploadCreateCertificationsErrorComponent
        | ApiV1ProvidersIconUploadCreateCriticalityErrorComponent
        | ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent
        | ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent
        | ApiV1ProvidersIconUploadCreateDebugModeErrorComponent
        | ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent
        | ApiV1ProvidersIconUploadCreateEmailsErrorComponent
        | ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent
        | ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent
        | ApiV1ProvidersIconUploadCreateKindErrorComponent
        | ApiV1ProvidersIconUploadCreateLabelsErrorComponent
        | ApiV1ProvidersIconUploadCreateLegalNameErrorComponent
        | ApiV1ProvidersIconUploadCreateNameErrorComponent
        | ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent
        | ApiV1ProvidersIconUploadCreatePhoneErrorComponent
        | ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent
        | ApiV1ProvidersIconUploadCreateProviderErrorComponent
        | ApiV1ProvidersIconUploadCreateProviderIdErrorComponent
        | ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent
        | ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent
        | ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent
        | ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent
        | ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent
        | ApiV1ProvidersIconUploadCreateSloTargetErrorComponent
        | ApiV1ProvidersIconUploadCreateSlugErrorComponent
        | ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent
        | ApiV1ProvidersIconUploadCreateTolerationsErrorComponent
        | ApiV1ProvidersIconUploadCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_icon_upload_create_active_error_component import (
            ApiV1ProvidersIconUploadCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_address_error_component import (
            ApiV1ProvidersIconUploadCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_annotations_error_component import (
            ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_at_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_reason_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_asn_error_component import (
            ApiV1ProvidersIconUploadCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_ccm_block_error_component import (
            ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_criticality_error_component import (
            ApiV1ProvidersIconUploadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_csi_controller_block_error_component import (
            ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_csi_storage_classes_error_component import (
            ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_debug_mode_error_component import (
            ApiV1ProvidersIconUploadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_display_name_error_component import (
            ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_emails_error_component import (
            ApiV1ProvidersIconUploadCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_icon_content_type_error_component import (
            ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_icon_filename_error_component import (
            ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_kind_error_component import (
            ApiV1ProvidersIconUploadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_labels_error_component import (
            ApiV1ProvidersIconUploadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_legal_name_error_component import (
            ApiV1ProvidersIconUploadCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_name_error_component import (
            ApiV1ProvidersIconUploadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_non_field_errors_error_component import (
            ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_phone_error_component import (
            ApiV1ProvidersIconUploadCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_platform_service_error_component import (
            ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_error_component import (
            ApiV1ProvidersIconUploadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_id_error_component import (
            ApiV1ProvidersIconUploadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_reference_error_component import (
            ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_sla_availability_error_component import (
            ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_sla_target_error_component import (
            ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slo_availability_error_component import (
            ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slo_target_error_component import (
            ApiV1ProvidersIconUploadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slug_error_component import (
            ApiV1ProvidersIconUploadCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_target_availability_error_component import (
            ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_tolerations_error_component import (
            ApiV1ProvidersIconUploadCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_urls_error_component import (
            ApiV1ProvidersIconUploadCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersIconUploadCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_providers_icon_upload_create_active_error_component import (
            ApiV1ProvidersIconUploadCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_address_error_component import (
            ApiV1ProvidersIconUploadCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_annotations_error_component import (
            ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_at_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_archived_reason_error_component import (
            ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_asn_error_component import (
            ApiV1ProvidersIconUploadCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_ccm_block_error_component import (
            ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_certifications_error_component import (
            ApiV1ProvidersIconUploadCreateCertificationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_criticality_error_component import (
            ApiV1ProvidersIconUploadCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_csi_controller_block_error_component import (
            ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_csi_storage_classes_error_component import (
            ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_debug_mode_error_component import (
            ApiV1ProvidersIconUploadCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_display_name_error_component import (
            ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_emails_error_component import (
            ApiV1ProvidersIconUploadCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_icon_content_type_error_component import (
            ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_icon_filename_error_component import (
            ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_kind_error_component import (
            ApiV1ProvidersIconUploadCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_labels_error_component import (
            ApiV1ProvidersIconUploadCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_legal_name_error_component import (
            ApiV1ProvidersIconUploadCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_name_error_component import (
            ApiV1ProvidersIconUploadCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_non_field_errors_error_component import (
            ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_phone_error_component import (
            ApiV1ProvidersIconUploadCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_platform_service_error_component import (
            ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_error_component import (
            ApiV1ProvidersIconUploadCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_id_error_component import (
            ApiV1ProvidersIconUploadCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_provider_reference_error_component import (
            ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_sla_availability_error_component import (
            ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_sla_target_error_component import (
            ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slo_availability_error_component import (
            ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slo_target_error_component import (
            ApiV1ProvidersIconUploadCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_slug_error_component import (
            ApiV1ProvidersIconUploadCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_target_availability_error_component import (
            ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_tolerations_error_component import (
            ApiV1ProvidersIconUploadCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_icon_upload_create_urls_error_component import (
            ApiV1ProvidersIconUploadCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersIconUploadCreateActiveErrorComponent
                | ApiV1ProvidersIconUploadCreateAddressErrorComponent
                | ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent
                | ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent
                | ApiV1ProvidersIconUploadCreateArchivedErrorComponent
                | ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent
                | ApiV1ProvidersIconUploadCreateAsnErrorComponent
                | ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent
                | ApiV1ProvidersIconUploadCreateCertificationsErrorComponent
                | ApiV1ProvidersIconUploadCreateCriticalityErrorComponent
                | ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent
                | ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent
                | ApiV1ProvidersIconUploadCreateDebugModeErrorComponent
                | ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent
                | ApiV1ProvidersIconUploadCreateEmailsErrorComponent
                | ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent
                | ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent
                | ApiV1ProvidersIconUploadCreateKindErrorComponent
                | ApiV1ProvidersIconUploadCreateLabelsErrorComponent
                | ApiV1ProvidersIconUploadCreateLegalNameErrorComponent
                | ApiV1ProvidersIconUploadCreateNameErrorComponent
                | ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent
                | ApiV1ProvidersIconUploadCreatePhoneErrorComponent
                | ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent
                | ApiV1ProvidersIconUploadCreateProviderErrorComponent
                | ApiV1ProvidersIconUploadCreateProviderIdErrorComponent
                | ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent
                | ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent
                | ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent
                | ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent
                | ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent
                | ApiV1ProvidersIconUploadCreateSloTargetErrorComponent
                | ApiV1ProvidersIconUploadCreateSlugErrorComponent
                | ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent
                | ApiV1ProvidersIconUploadCreateTolerationsErrorComponent
                | ApiV1ProvidersIconUploadCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_0 = (
                        ApiV1ProvidersIconUploadCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_1 = (
                        ApiV1ProvidersIconUploadCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_2 = (
                        ApiV1ProvidersIconUploadCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_3 = (
                        ApiV1ProvidersIconUploadCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_4 = (
                        ApiV1ProvidersIconUploadCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_5 = (
                        ApiV1ProvidersIconUploadCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_6 = (
                        ApiV1ProvidersIconUploadCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_7 = (
                        ApiV1ProvidersIconUploadCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_8 = (
                        ApiV1ProvidersIconUploadCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_9 = (
                        ApiV1ProvidersIconUploadCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_10 = (
                        ApiV1ProvidersIconUploadCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_11 = (
                        ApiV1ProvidersIconUploadCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_12 = (
                        ApiV1ProvidersIconUploadCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_13 = (
                        ApiV1ProvidersIconUploadCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_14 = (
                        ApiV1ProvidersIconUploadCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_15 = (
                        ApiV1ProvidersIconUploadCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_16 = (
                        ApiV1ProvidersIconUploadCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_17 = (
                        ApiV1ProvidersIconUploadCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_18 = (
                        ApiV1ProvidersIconUploadCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_19 = (
                        ApiV1ProvidersIconUploadCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_20 = (
                        ApiV1ProvidersIconUploadCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_21 = (
                        ApiV1ProvidersIconUploadCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_22 = (
                        ApiV1ProvidersIconUploadCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_23 = (
                        ApiV1ProvidersIconUploadCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_24 = (
                        ApiV1ProvidersIconUploadCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_25 = (
                        ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_26 = (
                        ApiV1ProvidersIconUploadCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_27 = (
                        ApiV1ProvidersIconUploadCreateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_28 = (
                        ApiV1ProvidersIconUploadCreateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_29 = (
                        ApiV1ProvidersIconUploadCreateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_30 = (
                        ApiV1ProvidersIconUploadCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_31 = (
                        ApiV1ProvidersIconUploadCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_32 = (
                        ApiV1ProvidersIconUploadCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_33 = (
                        ApiV1ProvidersIconUploadCreateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_icon_upload_create_error_type_34 = (
                        ApiV1ProvidersIconUploadCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_icon_upload_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_icon_upload_create_error_type_35 = (
                    ApiV1ProvidersIconUploadCreateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_icon_upload_create_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_icon_upload_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_icon_upload_create_validation_error.additional_properties = d
        return api_v1_providers_icon_upload_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
