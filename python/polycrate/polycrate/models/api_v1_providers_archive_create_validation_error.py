from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_archive_create_active_error_component import (
        ApiV1ProvidersArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_address_error_component import (
        ApiV1ProvidersArchiveCreateAddressErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_annotations_error_component import (
        ApiV1ProvidersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_archived_at_error_component import (
        ApiV1ProvidersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_archived_error_component import (
        ApiV1ProvidersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_archived_reason_error_component import (
        ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_asn_error_component import (
        ApiV1ProvidersArchiveCreateAsnErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_ccm_block_error_component import (
        ApiV1ProvidersArchiveCreateCcmBlockErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_certifications_error_component import (
        ApiV1ProvidersArchiveCreateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_criticality_error_component import (
        ApiV1ProvidersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_csi_controller_block_error_component import (
        ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_csi_storage_classes_error_component import (
        ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_debug_mode_error_component import (
        ApiV1ProvidersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_display_name_error_component import (
        ApiV1ProvidersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_emails_error_component import (
        ApiV1ProvidersArchiveCreateEmailsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_icon_content_type_error_component import (
        ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_icon_filename_error_component import (
        ApiV1ProvidersArchiveCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_kind_error_component import (
        ApiV1ProvidersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_labels_error_component import (
        ApiV1ProvidersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_legal_name_error_component import (
        ApiV1ProvidersArchiveCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_name_error_component import (
        ApiV1ProvidersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_non_field_errors_error_component import (
        ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_phone_error_component import (
        ApiV1ProvidersArchiveCreatePhoneErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_platform_service_error_component import (
        ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_provider_error_component import (
        ApiV1ProvidersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_provider_id_error_component import (
        ApiV1ProvidersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_provider_reference_error_component import (
        ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_reconciliation_enabled_error_component import (
        ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_sla_availability_error_component import (
        ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_sla_target_error_component import (
        ApiV1ProvidersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_slo_availability_error_component import (
        ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_slo_target_error_component import (
        ApiV1ProvidersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_slug_error_component import (
        ApiV1ProvidersArchiveCreateSlugErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_target_availability_error_component import (
        ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_tolerations_error_component import (
        ApiV1ProvidersArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_archive_create_urls_error_component import (
        ApiV1ProvidersArchiveCreateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProvidersArchiveCreateValidationError")


@_attrs_define
class ApiV1ProvidersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersArchiveCreateActiveErrorComponent | ApiV1ProvidersArchiveCreateAddressErrorComponent
            | ApiV1ProvidersArchiveCreateAnnotationsErrorComponent | ApiV1ProvidersArchiveCreateArchivedAtErrorComponent |
            ApiV1ProvidersArchiveCreateArchivedErrorComponent | ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent |
            ApiV1ProvidersArchiveCreateAsnErrorComponent | ApiV1ProvidersArchiveCreateCcmBlockErrorComponent |
            ApiV1ProvidersArchiveCreateCertificationsErrorComponent | ApiV1ProvidersArchiveCreateCriticalityErrorComponent |
            ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent |
            ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent | ApiV1ProvidersArchiveCreateDebugModeErrorComponent
            | ApiV1ProvidersArchiveCreateDisplayNameErrorComponent | ApiV1ProvidersArchiveCreateEmailsErrorComponent |
            ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent | ApiV1ProvidersArchiveCreateIconFilenameErrorComponent
            | ApiV1ProvidersArchiveCreateKindErrorComponent | ApiV1ProvidersArchiveCreateLabelsErrorComponent |
            ApiV1ProvidersArchiveCreateLegalNameErrorComponent | ApiV1ProvidersArchiveCreateNameErrorComponent |
            ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent | ApiV1ProvidersArchiveCreatePhoneErrorComponent |
            ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent | ApiV1ProvidersArchiveCreateProviderErrorComponent |
            ApiV1ProvidersArchiveCreateProviderIdErrorComponent | ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent
            | ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent | ApiV1ProvidersArchiveCreateSlaTargetErrorComponent |
            ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent | ApiV1ProvidersArchiveCreateSloTargetErrorComponent |
            ApiV1ProvidersArchiveCreateSlugErrorComponent | ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ProvidersArchiveCreateTolerationsErrorComponent | ApiV1ProvidersArchiveCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersArchiveCreateActiveErrorComponent
        | ApiV1ProvidersArchiveCreateAddressErrorComponent
        | ApiV1ProvidersArchiveCreateAnnotationsErrorComponent
        | ApiV1ProvidersArchiveCreateArchivedAtErrorComponent
        | ApiV1ProvidersArchiveCreateArchivedErrorComponent
        | ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent
        | ApiV1ProvidersArchiveCreateAsnErrorComponent
        | ApiV1ProvidersArchiveCreateCcmBlockErrorComponent
        | ApiV1ProvidersArchiveCreateCertificationsErrorComponent
        | ApiV1ProvidersArchiveCreateCriticalityErrorComponent
        | ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent
        | ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent
        | ApiV1ProvidersArchiveCreateDebugModeErrorComponent
        | ApiV1ProvidersArchiveCreateDisplayNameErrorComponent
        | ApiV1ProvidersArchiveCreateEmailsErrorComponent
        | ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent
        | ApiV1ProvidersArchiveCreateIconFilenameErrorComponent
        | ApiV1ProvidersArchiveCreateKindErrorComponent
        | ApiV1ProvidersArchiveCreateLabelsErrorComponent
        | ApiV1ProvidersArchiveCreateLegalNameErrorComponent
        | ApiV1ProvidersArchiveCreateNameErrorComponent
        | ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ProvidersArchiveCreatePhoneErrorComponent
        | ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent
        | ApiV1ProvidersArchiveCreateProviderErrorComponent
        | ApiV1ProvidersArchiveCreateProviderIdErrorComponent
        | ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent
        | ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ProvidersArchiveCreateSlaTargetErrorComponent
        | ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ProvidersArchiveCreateSloTargetErrorComponent
        | ApiV1ProvidersArchiveCreateSlugErrorComponent
        | ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ProvidersArchiveCreateTolerationsErrorComponent
        | ApiV1ProvidersArchiveCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_archive_create_active_error_component import (
            ApiV1ProvidersArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_address_error_component import (
            ApiV1ProvidersArchiveCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_annotations_error_component import (
            ApiV1ProvidersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_at_error_component import (
            ApiV1ProvidersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_error_component import (
            ApiV1ProvidersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_reason_error_component import (
            ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_asn_error_component import (
            ApiV1ProvidersArchiveCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_ccm_block_error_component import (
            ApiV1ProvidersArchiveCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_criticality_error_component import (
            ApiV1ProvidersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_csi_controller_block_error_component import (
            ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_csi_storage_classes_error_component import (
            ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_debug_mode_error_component import (
            ApiV1ProvidersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_display_name_error_component import (
            ApiV1ProvidersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_emails_error_component import (
            ApiV1ProvidersArchiveCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_icon_content_type_error_component import (
            ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_icon_filename_error_component import (
            ApiV1ProvidersArchiveCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_kind_error_component import (
            ApiV1ProvidersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_labels_error_component import (
            ApiV1ProvidersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_legal_name_error_component import (
            ApiV1ProvidersArchiveCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_name_error_component import (
            ApiV1ProvidersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_non_field_errors_error_component import (
            ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_phone_error_component import (
            ApiV1ProvidersArchiveCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_platform_service_error_component import (
            ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_error_component import (
            ApiV1ProvidersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_id_error_component import (
            ApiV1ProvidersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_reference_error_component import (
            ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_sla_availability_error_component import (
            ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_sla_target_error_component import (
            ApiV1ProvidersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slo_availability_error_component import (
            ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slo_target_error_component import (
            ApiV1ProvidersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slug_error_component import (
            ApiV1ProvidersArchiveCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_target_availability_error_component import (
            ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_tolerations_error_component import (
            ApiV1ProvidersArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_urls_error_component import (
            ApiV1ProvidersArchiveCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersArchiveCreateUrlsErrorComponent):
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
        from ..models.api_v1_providers_archive_create_active_error_component import (
            ApiV1ProvidersArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_address_error_component import (
            ApiV1ProvidersArchiveCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_annotations_error_component import (
            ApiV1ProvidersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_at_error_component import (
            ApiV1ProvidersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_error_component import (
            ApiV1ProvidersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_archived_reason_error_component import (
            ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_asn_error_component import (
            ApiV1ProvidersArchiveCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_ccm_block_error_component import (
            ApiV1ProvidersArchiveCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_certifications_error_component import (
            ApiV1ProvidersArchiveCreateCertificationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_criticality_error_component import (
            ApiV1ProvidersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_csi_controller_block_error_component import (
            ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_csi_storage_classes_error_component import (
            ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_debug_mode_error_component import (
            ApiV1ProvidersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_display_name_error_component import (
            ApiV1ProvidersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_emails_error_component import (
            ApiV1ProvidersArchiveCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_icon_content_type_error_component import (
            ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_icon_filename_error_component import (
            ApiV1ProvidersArchiveCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_kind_error_component import (
            ApiV1ProvidersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_labels_error_component import (
            ApiV1ProvidersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_legal_name_error_component import (
            ApiV1ProvidersArchiveCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_name_error_component import (
            ApiV1ProvidersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_non_field_errors_error_component import (
            ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_phone_error_component import (
            ApiV1ProvidersArchiveCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_platform_service_error_component import (
            ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_error_component import (
            ApiV1ProvidersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_id_error_component import (
            ApiV1ProvidersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_provider_reference_error_component import (
            ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_sla_availability_error_component import (
            ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_sla_target_error_component import (
            ApiV1ProvidersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slo_availability_error_component import (
            ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slo_target_error_component import (
            ApiV1ProvidersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_slug_error_component import (
            ApiV1ProvidersArchiveCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_target_availability_error_component import (
            ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_tolerations_error_component import (
            ApiV1ProvidersArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_archive_create_urls_error_component import (
            ApiV1ProvidersArchiveCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersArchiveCreateActiveErrorComponent
                | ApiV1ProvidersArchiveCreateAddressErrorComponent
                | ApiV1ProvidersArchiveCreateAnnotationsErrorComponent
                | ApiV1ProvidersArchiveCreateArchivedAtErrorComponent
                | ApiV1ProvidersArchiveCreateArchivedErrorComponent
                | ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent
                | ApiV1ProvidersArchiveCreateAsnErrorComponent
                | ApiV1ProvidersArchiveCreateCcmBlockErrorComponent
                | ApiV1ProvidersArchiveCreateCertificationsErrorComponent
                | ApiV1ProvidersArchiveCreateCriticalityErrorComponent
                | ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent
                | ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent
                | ApiV1ProvidersArchiveCreateDebugModeErrorComponent
                | ApiV1ProvidersArchiveCreateDisplayNameErrorComponent
                | ApiV1ProvidersArchiveCreateEmailsErrorComponent
                | ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent
                | ApiV1ProvidersArchiveCreateIconFilenameErrorComponent
                | ApiV1ProvidersArchiveCreateKindErrorComponent
                | ApiV1ProvidersArchiveCreateLabelsErrorComponent
                | ApiV1ProvidersArchiveCreateLegalNameErrorComponent
                | ApiV1ProvidersArchiveCreateNameErrorComponent
                | ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ProvidersArchiveCreatePhoneErrorComponent
                | ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent
                | ApiV1ProvidersArchiveCreateProviderErrorComponent
                | ApiV1ProvidersArchiveCreateProviderIdErrorComponent
                | ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent
                | ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ProvidersArchiveCreateSlaTargetErrorComponent
                | ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ProvidersArchiveCreateSloTargetErrorComponent
                | ApiV1ProvidersArchiveCreateSlugErrorComponent
                | ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ProvidersArchiveCreateTolerationsErrorComponent
                | ApiV1ProvidersArchiveCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_0 = (
                        ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_1 = (
                        ApiV1ProvidersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_2 = (
                        ApiV1ProvidersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_3 = (
                        ApiV1ProvidersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_4 = (
                        ApiV1ProvidersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_5 = (
                        ApiV1ProvidersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_6 = (
                        ApiV1ProvidersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_7 = (
                        ApiV1ProvidersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_8 = (
                        ApiV1ProvidersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_9 = (
                        ApiV1ProvidersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_10 = (
                        ApiV1ProvidersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_11 = (
                        ApiV1ProvidersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_12 = (
                        ApiV1ProvidersArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_13 = (
                        ApiV1ProvidersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_14 = (
                        ApiV1ProvidersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_15 = (
                        ApiV1ProvidersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_16 = (
                        ApiV1ProvidersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_17 = (
                        ApiV1ProvidersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_18 = (
                        ApiV1ProvidersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_19 = (
                        ApiV1ProvidersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_20 = (
                        ApiV1ProvidersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_21 = (
                        ApiV1ProvidersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_22 = (
                        ApiV1ProvidersArchiveCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_23 = (
                        ApiV1ProvidersArchiveCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_24 = (
                        ApiV1ProvidersArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_25 = (
                        ApiV1ProvidersArchiveCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_26 = (
                        ApiV1ProvidersArchiveCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_27 = (
                        ApiV1ProvidersArchiveCreateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_28 = (
                        ApiV1ProvidersArchiveCreateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_29 = (
                        ApiV1ProvidersArchiveCreateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_30 = (
                        ApiV1ProvidersArchiveCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_31 = (
                        ApiV1ProvidersArchiveCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_32 = (
                        ApiV1ProvidersArchiveCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_33 = (
                        ApiV1ProvidersArchiveCreateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_archive_create_error_type_34 = (
                        ApiV1ProvidersArchiveCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_archive_create_error_type_35 = (
                    ApiV1ProvidersArchiveCreateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_archive_create_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_archive_create_validation_error.additional_properties = d
        return api_v1_providers_archive_create_validation_error

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
