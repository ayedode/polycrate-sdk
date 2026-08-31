from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_partial_update_active_error_component import (
        ApiV1ProvidersPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_address_error_component import (
        ApiV1ProvidersPartialUpdateAddressErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_annotations_error_component import (
        ApiV1ProvidersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_archived_at_error_component import (
        ApiV1ProvidersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_archived_error_component import (
        ApiV1ProvidersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_archived_reason_error_component import (
        ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_asn_error_component import (
        ApiV1ProvidersPartialUpdateAsnErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_ccm_block_error_component import (
        ApiV1ProvidersPartialUpdateCcmBlockErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_certifications_error_component import (
        ApiV1ProvidersPartialUpdateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_criticality_error_component import (
        ApiV1ProvidersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_csi_controller_block_error_component import (
        ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_csi_storage_classes_error_component import (
        ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_debug_mode_error_component import (
        ApiV1ProvidersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_display_name_error_component import (
        ApiV1ProvidersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_emails_error_component import (
        ApiV1ProvidersPartialUpdateEmailsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_icon_content_type_error_component import (
        ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_icon_filename_error_component import (
        ApiV1ProvidersPartialUpdateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_kind_error_component import (
        ApiV1ProvidersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_labels_error_component import (
        ApiV1ProvidersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_legal_name_error_component import (
        ApiV1ProvidersPartialUpdateLegalNameErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_name_error_component import (
        ApiV1ProvidersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_non_field_errors_error_component import (
        ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_phone_error_component import (
        ApiV1ProvidersPartialUpdatePhoneErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_platform_service_error_component import (
        ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_provider_error_component import (
        ApiV1ProvidersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_provider_id_error_component import (
        ApiV1ProvidersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_provider_reference_error_component import (
        ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_reconciliation_enabled_error_component import (
        ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_sla_availability_error_component import (
        ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_sla_target_error_component import (
        ApiV1ProvidersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_slo_availability_error_component import (
        ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_slo_target_error_component import (
        ApiV1ProvidersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_slug_error_component import (
        ApiV1ProvidersPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_target_availability_error_component import (
        ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_tolerations_error_component import (
        ApiV1ProvidersPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_partial_update_urls_error_component import (
        ApiV1ProvidersPartialUpdateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProvidersPartialUpdateValidationError")


@_attrs_define
class ApiV1ProvidersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersPartialUpdateActiveErrorComponent | ApiV1ProvidersPartialUpdateAddressErrorComponent
            | ApiV1ProvidersPartialUpdateAnnotationsErrorComponent | ApiV1ProvidersPartialUpdateArchivedAtErrorComponent |
            ApiV1ProvidersPartialUpdateArchivedErrorComponent | ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent |
            ApiV1ProvidersPartialUpdateAsnErrorComponent | ApiV1ProvidersPartialUpdateCcmBlockErrorComponent |
            ApiV1ProvidersPartialUpdateCertificationsErrorComponent | ApiV1ProvidersPartialUpdateCriticalityErrorComponent |
            ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent |
            ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent | ApiV1ProvidersPartialUpdateDebugModeErrorComponent
            | ApiV1ProvidersPartialUpdateDisplayNameErrorComponent | ApiV1ProvidersPartialUpdateEmailsErrorComponent |
            ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent | ApiV1ProvidersPartialUpdateIconFilenameErrorComponent
            | ApiV1ProvidersPartialUpdateKindErrorComponent | ApiV1ProvidersPartialUpdateLabelsErrorComponent |
            ApiV1ProvidersPartialUpdateLegalNameErrorComponent | ApiV1ProvidersPartialUpdateNameErrorComponent |
            ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent | ApiV1ProvidersPartialUpdatePhoneErrorComponent |
            ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent | ApiV1ProvidersPartialUpdateProviderErrorComponent |
            ApiV1ProvidersPartialUpdateProviderIdErrorComponent | ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent
            | ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent | ApiV1ProvidersPartialUpdateSlaTargetErrorComponent |
            ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent | ApiV1ProvidersPartialUpdateSloTargetErrorComponent |
            ApiV1ProvidersPartialUpdateSlugErrorComponent | ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ProvidersPartialUpdateTolerationsErrorComponent | ApiV1ProvidersPartialUpdateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersPartialUpdateActiveErrorComponent
        | ApiV1ProvidersPartialUpdateAddressErrorComponent
        | ApiV1ProvidersPartialUpdateAnnotationsErrorComponent
        | ApiV1ProvidersPartialUpdateArchivedAtErrorComponent
        | ApiV1ProvidersPartialUpdateArchivedErrorComponent
        | ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent
        | ApiV1ProvidersPartialUpdateAsnErrorComponent
        | ApiV1ProvidersPartialUpdateCcmBlockErrorComponent
        | ApiV1ProvidersPartialUpdateCertificationsErrorComponent
        | ApiV1ProvidersPartialUpdateCriticalityErrorComponent
        | ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent
        | ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent
        | ApiV1ProvidersPartialUpdateDebugModeErrorComponent
        | ApiV1ProvidersPartialUpdateDisplayNameErrorComponent
        | ApiV1ProvidersPartialUpdateEmailsErrorComponent
        | ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent
        | ApiV1ProvidersPartialUpdateIconFilenameErrorComponent
        | ApiV1ProvidersPartialUpdateKindErrorComponent
        | ApiV1ProvidersPartialUpdateLabelsErrorComponent
        | ApiV1ProvidersPartialUpdateLegalNameErrorComponent
        | ApiV1ProvidersPartialUpdateNameErrorComponent
        | ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ProvidersPartialUpdatePhoneErrorComponent
        | ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent
        | ApiV1ProvidersPartialUpdateProviderErrorComponent
        | ApiV1ProvidersPartialUpdateProviderIdErrorComponent
        | ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent
        | ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ProvidersPartialUpdateSlaTargetErrorComponent
        | ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ProvidersPartialUpdateSloTargetErrorComponent
        | ApiV1ProvidersPartialUpdateSlugErrorComponent
        | ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ProvidersPartialUpdateTolerationsErrorComponent
        | ApiV1ProvidersPartialUpdateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_partial_update_active_error_component import (
            ApiV1ProvidersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_address_error_component import (
            ApiV1ProvidersPartialUpdateAddressErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_annotations_error_component import (
            ApiV1ProvidersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_at_error_component import (
            ApiV1ProvidersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_error_component import (
            ApiV1ProvidersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_reason_error_component import (
            ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_asn_error_component import (
            ApiV1ProvidersPartialUpdateAsnErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_ccm_block_error_component import (
            ApiV1ProvidersPartialUpdateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_criticality_error_component import (
            ApiV1ProvidersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_csi_controller_block_error_component import (
            ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_csi_storage_classes_error_component import (
            ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_debug_mode_error_component import (
            ApiV1ProvidersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_display_name_error_component import (
            ApiV1ProvidersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_emails_error_component import (
            ApiV1ProvidersPartialUpdateEmailsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_icon_content_type_error_component import (
            ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_icon_filename_error_component import (
            ApiV1ProvidersPartialUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_kind_error_component import (
            ApiV1ProvidersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_labels_error_component import (
            ApiV1ProvidersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_legal_name_error_component import (
            ApiV1ProvidersPartialUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_name_error_component import (
            ApiV1ProvidersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_non_field_errors_error_component import (
            ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_phone_error_component import (
            ApiV1ProvidersPartialUpdatePhoneErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_platform_service_error_component import (
            ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_error_component import (
            ApiV1ProvidersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_id_error_component import (
            ApiV1ProvidersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_reference_error_component import (
            ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_sla_availability_error_component import (
            ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_sla_target_error_component import (
            ApiV1ProvidersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slo_availability_error_component import (
            ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slo_target_error_component import (
            ApiV1ProvidersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slug_error_component import (
            ApiV1ProvidersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_target_availability_error_component import (
            ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_tolerations_error_component import (
            ApiV1ProvidersPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_urls_error_component import (
            ApiV1ProvidersPartialUpdateUrlsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersPartialUpdateUrlsErrorComponent):
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
        from ..models.api_v1_providers_partial_update_active_error_component import (
            ApiV1ProvidersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_address_error_component import (
            ApiV1ProvidersPartialUpdateAddressErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_annotations_error_component import (
            ApiV1ProvidersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_at_error_component import (
            ApiV1ProvidersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_error_component import (
            ApiV1ProvidersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_archived_reason_error_component import (
            ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_asn_error_component import (
            ApiV1ProvidersPartialUpdateAsnErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_ccm_block_error_component import (
            ApiV1ProvidersPartialUpdateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_certifications_error_component import (
            ApiV1ProvidersPartialUpdateCertificationsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_criticality_error_component import (
            ApiV1ProvidersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_csi_controller_block_error_component import (
            ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_csi_storage_classes_error_component import (
            ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_debug_mode_error_component import (
            ApiV1ProvidersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_display_name_error_component import (
            ApiV1ProvidersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_emails_error_component import (
            ApiV1ProvidersPartialUpdateEmailsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_icon_content_type_error_component import (
            ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_icon_filename_error_component import (
            ApiV1ProvidersPartialUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_kind_error_component import (
            ApiV1ProvidersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_labels_error_component import (
            ApiV1ProvidersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_legal_name_error_component import (
            ApiV1ProvidersPartialUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_name_error_component import (
            ApiV1ProvidersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_non_field_errors_error_component import (
            ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_phone_error_component import (
            ApiV1ProvidersPartialUpdatePhoneErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_platform_service_error_component import (
            ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_error_component import (
            ApiV1ProvidersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_id_error_component import (
            ApiV1ProvidersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_provider_reference_error_component import (
            ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_sla_availability_error_component import (
            ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_sla_target_error_component import (
            ApiV1ProvidersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slo_availability_error_component import (
            ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slo_target_error_component import (
            ApiV1ProvidersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_slug_error_component import (
            ApiV1ProvidersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_target_availability_error_component import (
            ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_tolerations_error_component import (
            ApiV1ProvidersPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_partial_update_urls_error_component import (
            ApiV1ProvidersPartialUpdateUrlsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersPartialUpdateActiveErrorComponent
                | ApiV1ProvidersPartialUpdateAddressErrorComponent
                | ApiV1ProvidersPartialUpdateAnnotationsErrorComponent
                | ApiV1ProvidersPartialUpdateArchivedAtErrorComponent
                | ApiV1ProvidersPartialUpdateArchivedErrorComponent
                | ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent
                | ApiV1ProvidersPartialUpdateAsnErrorComponent
                | ApiV1ProvidersPartialUpdateCcmBlockErrorComponent
                | ApiV1ProvidersPartialUpdateCertificationsErrorComponent
                | ApiV1ProvidersPartialUpdateCriticalityErrorComponent
                | ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent
                | ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent
                | ApiV1ProvidersPartialUpdateDebugModeErrorComponent
                | ApiV1ProvidersPartialUpdateDisplayNameErrorComponent
                | ApiV1ProvidersPartialUpdateEmailsErrorComponent
                | ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent
                | ApiV1ProvidersPartialUpdateIconFilenameErrorComponent
                | ApiV1ProvidersPartialUpdateKindErrorComponent
                | ApiV1ProvidersPartialUpdateLabelsErrorComponent
                | ApiV1ProvidersPartialUpdateLegalNameErrorComponent
                | ApiV1ProvidersPartialUpdateNameErrorComponent
                | ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ProvidersPartialUpdatePhoneErrorComponent
                | ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent
                | ApiV1ProvidersPartialUpdateProviderErrorComponent
                | ApiV1ProvidersPartialUpdateProviderIdErrorComponent
                | ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent
                | ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ProvidersPartialUpdateSlaTargetErrorComponent
                | ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ProvidersPartialUpdateSloTargetErrorComponent
                | ApiV1ProvidersPartialUpdateSlugErrorComponent
                | ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ProvidersPartialUpdateTolerationsErrorComponent
                | ApiV1ProvidersPartialUpdateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_0 = (
                        ApiV1ProvidersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_1 = (
                        ApiV1ProvidersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_2 = (
                        ApiV1ProvidersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_3 = (
                        ApiV1ProvidersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_4 = (
                        ApiV1ProvidersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_5 = (
                        ApiV1ProvidersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_6 = (
                        ApiV1ProvidersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_7 = (
                        ApiV1ProvidersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_8 = (
                        ApiV1ProvidersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_9 = (
                        ApiV1ProvidersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_10 = (
                        ApiV1ProvidersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_11 = (
                        ApiV1ProvidersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_12 = (
                        ApiV1ProvidersPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_13 = (
                        ApiV1ProvidersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_14 = (
                        ApiV1ProvidersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_15 = (
                        ApiV1ProvidersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_16 = (
                        ApiV1ProvidersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_17 = (
                        ApiV1ProvidersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_18 = (
                        ApiV1ProvidersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_19 = (
                        ApiV1ProvidersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_20 = (
                        ApiV1ProvidersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_21 = (
                        ApiV1ProvidersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_22 = (
                        ApiV1ProvidersPartialUpdateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_23 = (
                        ApiV1ProvidersPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_24 = (
                        ApiV1ProvidersPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_25 = (
                        ApiV1ProvidersPartialUpdateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_26 = (
                        ApiV1ProvidersPartialUpdateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_27 = (
                        ApiV1ProvidersPartialUpdateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_28 = (
                        ApiV1ProvidersPartialUpdateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_29 = (
                        ApiV1ProvidersPartialUpdateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_30 = (
                        ApiV1ProvidersPartialUpdateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_31 = (
                        ApiV1ProvidersPartialUpdateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_32 = (
                        ApiV1ProvidersPartialUpdatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_33 = (
                        ApiV1ProvidersPartialUpdateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_partial_update_error_type_34 = (
                        ApiV1ProvidersPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_partial_update_error_type_35 = (
                    ApiV1ProvidersPartialUpdateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_partial_update_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_partial_update_validation_error.additional_properties = d
        return api_v1_providers_partial_update_validation_error

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
