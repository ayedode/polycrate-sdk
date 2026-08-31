from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_update_active_error_component import ApiV1ProvidersUpdateActiveErrorComponent
    from ..models.api_v1_providers_update_address_error_component import ApiV1ProvidersUpdateAddressErrorComponent
    from ..models.api_v1_providers_update_annotations_error_component import (
        ApiV1ProvidersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_update_archived_at_error_component import (
        ApiV1ProvidersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_update_archived_error_component import ApiV1ProvidersUpdateArchivedErrorComponent
    from ..models.api_v1_providers_update_archived_reason_error_component import (
        ApiV1ProvidersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_update_asn_error_component import ApiV1ProvidersUpdateAsnErrorComponent
    from ..models.api_v1_providers_update_ccm_block_error_component import ApiV1ProvidersUpdateCcmBlockErrorComponent
    from ..models.api_v1_providers_update_certifications_error_component import (
        ApiV1ProvidersUpdateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_update_criticality_error_component import (
        ApiV1ProvidersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_update_csi_controller_block_error_component import (
        ApiV1ProvidersUpdateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_update_csi_storage_classes_error_component import (
        ApiV1ProvidersUpdateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_update_debug_mode_error_component import ApiV1ProvidersUpdateDebugModeErrorComponent
    from ..models.api_v1_providers_update_display_name_error_component import (
        ApiV1ProvidersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_update_emails_error_component import ApiV1ProvidersUpdateEmailsErrorComponent
    from ..models.api_v1_providers_update_icon_content_type_error_component import (
        ApiV1ProvidersUpdateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_update_icon_filename_error_component import (
        ApiV1ProvidersUpdateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_update_kind_error_component import ApiV1ProvidersUpdateKindErrorComponent
    from ..models.api_v1_providers_update_labels_error_component import ApiV1ProvidersUpdateLabelsErrorComponent
    from ..models.api_v1_providers_update_legal_name_error_component import ApiV1ProvidersUpdateLegalNameErrorComponent
    from ..models.api_v1_providers_update_name_error_component import ApiV1ProvidersUpdateNameErrorComponent
    from ..models.api_v1_providers_update_non_field_errors_error_component import (
        ApiV1ProvidersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_update_phone_error_component import ApiV1ProvidersUpdatePhoneErrorComponent
    from ..models.api_v1_providers_update_platform_service_error_component import (
        ApiV1ProvidersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_update_provider_error_component import ApiV1ProvidersUpdateProviderErrorComponent
    from ..models.api_v1_providers_update_provider_id_error_component import (
        ApiV1ProvidersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_update_provider_reference_error_component import (
        ApiV1ProvidersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_update_reconciliation_enabled_error_component import (
        ApiV1ProvidersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_update_sla_availability_error_component import (
        ApiV1ProvidersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_update_sla_target_error_component import ApiV1ProvidersUpdateSlaTargetErrorComponent
    from ..models.api_v1_providers_update_slo_availability_error_component import (
        ApiV1ProvidersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_update_slo_target_error_component import ApiV1ProvidersUpdateSloTargetErrorComponent
    from ..models.api_v1_providers_update_slug_error_component import ApiV1ProvidersUpdateSlugErrorComponent
    from ..models.api_v1_providers_update_target_availability_error_component import (
        ApiV1ProvidersUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_update_tolerations_error_component import (
        ApiV1ProvidersUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_update_urls_error_component import ApiV1ProvidersUpdateUrlsErrorComponent


T = TypeVar("T", bound="ApiV1ProvidersUpdateValidationError")


@_attrs_define
class ApiV1ProvidersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersUpdateActiveErrorComponent | ApiV1ProvidersUpdateAddressErrorComponent |
            ApiV1ProvidersUpdateAnnotationsErrorComponent | ApiV1ProvidersUpdateArchivedAtErrorComponent |
            ApiV1ProvidersUpdateArchivedErrorComponent | ApiV1ProvidersUpdateArchivedReasonErrorComponent |
            ApiV1ProvidersUpdateAsnErrorComponent | ApiV1ProvidersUpdateCcmBlockErrorComponent |
            ApiV1ProvidersUpdateCertificationsErrorComponent | ApiV1ProvidersUpdateCriticalityErrorComponent |
            ApiV1ProvidersUpdateCsiControllerBlockErrorComponent | ApiV1ProvidersUpdateCsiStorageClassesErrorComponent |
            ApiV1ProvidersUpdateDebugModeErrorComponent | ApiV1ProvidersUpdateDisplayNameErrorComponent |
            ApiV1ProvidersUpdateEmailsErrorComponent | ApiV1ProvidersUpdateIconContentTypeErrorComponent |
            ApiV1ProvidersUpdateIconFilenameErrorComponent | ApiV1ProvidersUpdateKindErrorComponent |
            ApiV1ProvidersUpdateLabelsErrorComponent | ApiV1ProvidersUpdateLegalNameErrorComponent |
            ApiV1ProvidersUpdateNameErrorComponent | ApiV1ProvidersUpdateNonFieldErrorsErrorComponent |
            ApiV1ProvidersUpdatePhoneErrorComponent | ApiV1ProvidersUpdatePlatformServiceErrorComponent |
            ApiV1ProvidersUpdateProviderErrorComponent | ApiV1ProvidersUpdateProviderIdErrorComponent |
            ApiV1ProvidersUpdateProviderReferenceErrorComponent | ApiV1ProvidersUpdateReconciliationEnabledErrorComponent |
            ApiV1ProvidersUpdateSlaAvailabilityErrorComponent | ApiV1ProvidersUpdateSlaTargetErrorComponent |
            ApiV1ProvidersUpdateSloAvailabilityErrorComponent | ApiV1ProvidersUpdateSloTargetErrorComponent |
            ApiV1ProvidersUpdateSlugErrorComponent | ApiV1ProvidersUpdateTargetAvailabilityErrorComponent |
            ApiV1ProvidersUpdateTolerationsErrorComponent | ApiV1ProvidersUpdateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersUpdateActiveErrorComponent
        | ApiV1ProvidersUpdateAddressErrorComponent
        | ApiV1ProvidersUpdateAnnotationsErrorComponent
        | ApiV1ProvidersUpdateArchivedAtErrorComponent
        | ApiV1ProvidersUpdateArchivedErrorComponent
        | ApiV1ProvidersUpdateArchivedReasonErrorComponent
        | ApiV1ProvidersUpdateAsnErrorComponent
        | ApiV1ProvidersUpdateCcmBlockErrorComponent
        | ApiV1ProvidersUpdateCertificationsErrorComponent
        | ApiV1ProvidersUpdateCriticalityErrorComponent
        | ApiV1ProvidersUpdateCsiControllerBlockErrorComponent
        | ApiV1ProvidersUpdateCsiStorageClassesErrorComponent
        | ApiV1ProvidersUpdateDebugModeErrorComponent
        | ApiV1ProvidersUpdateDisplayNameErrorComponent
        | ApiV1ProvidersUpdateEmailsErrorComponent
        | ApiV1ProvidersUpdateIconContentTypeErrorComponent
        | ApiV1ProvidersUpdateIconFilenameErrorComponent
        | ApiV1ProvidersUpdateKindErrorComponent
        | ApiV1ProvidersUpdateLabelsErrorComponent
        | ApiV1ProvidersUpdateLegalNameErrorComponent
        | ApiV1ProvidersUpdateNameErrorComponent
        | ApiV1ProvidersUpdateNonFieldErrorsErrorComponent
        | ApiV1ProvidersUpdatePhoneErrorComponent
        | ApiV1ProvidersUpdatePlatformServiceErrorComponent
        | ApiV1ProvidersUpdateProviderErrorComponent
        | ApiV1ProvidersUpdateProviderIdErrorComponent
        | ApiV1ProvidersUpdateProviderReferenceErrorComponent
        | ApiV1ProvidersUpdateReconciliationEnabledErrorComponent
        | ApiV1ProvidersUpdateSlaAvailabilityErrorComponent
        | ApiV1ProvidersUpdateSlaTargetErrorComponent
        | ApiV1ProvidersUpdateSloAvailabilityErrorComponent
        | ApiV1ProvidersUpdateSloTargetErrorComponent
        | ApiV1ProvidersUpdateSlugErrorComponent
        | ApiV1ProvidersUpdateTargetAvailabilityErrorComponent
        | ApiV1ProvidersUpdateTolerationsErrorComponent
        | ApiV1ProvidersUpdateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_update_active_error_component import ApiV1ProvidersUpdateActiveErrorComponent
        from ..models.api_v1_providers_update_address_error_component import ApiV1ProvidersUpdateAddressErrorComponent
        from ..models.api_v1_providers_update_annotations_error_component import (
            ApiV1ProvidersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_update_archived_at_error_component import (
            ApiV1ProvidersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_update_archived_error_component import ApiV1ProvidersUpdateArchivedErrorComponent
        from ..models.api_v1_providers_update_archived_reason_error_component import (
            ApiV1ProvidersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_update_asn_error_component import ApiV1ProvidersUpdateAsnErrorComponent
        from ..models.api_v1_providers_update_ccm_block_error_component import (
            ApiV1ProvidersUpdateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_update_criticality_error_component import (
            ApiV1ProvidersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_update_csi_controller_block_error_component import (
            ApiV1ProvidersUpdateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_update_csi_storage_classes_error_component import (
            ApiV1ProvidersUpdateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_update_debug_mode_error_component import (
            ApiV1ProvidersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_update_display_name_error_component import (
            ApiV1ProvidersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_update_emails_error_component import ApiV1ProvidersUpdateEmailsErrorComponent
        from ..models.api_v1_providers_update_icon_content_type_error_component import (
            ApiV1ProvidersUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_update_icon_filename_error_component import (
            ApiV1ProvidersUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_update_kind_error_component import ApiV1ProvidersUpdateKindErrorComponent
        from ..models.api_v1_providers_update_labels_error_component import ApiV1ProvidersUpdateLabelsErrorComponent
        from ..models.api_v1_providers_update_legal_name_error_component import (
            ApiV1ProvidersUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_update_name_error_component import ApiV1ProvidersUpdateNameErrorComponent
        from ..models.api_v1_providers_update_non_field_errors_error_component import (
            ApiV1ProvidersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_update_phone_error_component import ApiV1ProvidersUpdatePhoneErrorComponent
        from ..models.api_v1_providers_update_platform_service_error_component import (
            ApiV1ProvidersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_update_provider_error_component import ApiV1ProvidersUpdateProviderErrorComponent
        from ..models.api_v1_providers_update_provider_id_error_component import (
            ApiV1ProvidersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_update_provider_reference_error_component import (
            ApiV1ProvidersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_update_reconciliation_enabled_error_component import (
            ApiV1ProvidersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_update_sla_availability_error_component import (
            ApiV1ProvidersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_sla_target_error_component import (
            ApiV1ProvidersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_update_slo_availability_error_component import (
            ApiV1ProvidersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_slo_target_error_component import (
            ApiV1ProvidersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_update_slug_error_component import ApiV1ProvidersUpdateSlugErrorComponent
        from ..models.api_v1_providers_update_target_availability_error_component import (
            ApiV1ProvidersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_tolerations_error_component import (
            ApiV1ProvidersUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_update_urls_error_component import ApiV1ProvidersUpdateUrlsErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersUpdateUrlsErrorComponent):
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
        from ..models.api_v1_providers_update_active_error_component import ApiV1ProvidersUpdateActiveErrorComponent
        from ..models.api_v1_providers_update_address_error_component import ApiV1ProvidersUpdateAddressErrorComponent
        from ..models.api_v1_providers_update_annotations_error_component import (
            ApiV1ProvidersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_update_archived_at_error_component import (
            ApiV1ProvidersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_update_archived_error_component import ApiV1ProvidersUpdateArchivedErrorComponent
        from ..models.api_v1_providers_update_archived_reason_error_component import (
            ApiV1ProvidersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_update_asn_error_component import ApiV1ProvidersUpdateAsnErrorComponent
        from ..models.api_v1_providers_update_ccm_block_error_component import (
            ApiV1ProvidersUpdateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_update_certifications_error_component import (
            ApiV1ProvidersUpdateCertificationsErrorComponent,
        )
        from ..models.api_v1_providers_update_criticality_error_component import (
            ApiV1ProvidersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_update_csi_controller_block_error_component import (
            ApiV1ProvidersUpdateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_update_csi_storage_classes_error_component import (
            ApiV1ProvidersUpdateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_update_debug_mode_error_component import (
            ApiV1ProvidersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_update_display_name_error_component import (
            ApiV1ProvidersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_update_emails_error_component import ApiV1ProvidersUpdateEmailsErrorComponent
        from ..models.api_v1_providers_update_icon_content_type_error_component import (
            ApiV1ProvidersUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_update_icon_filename_error_component import (
            ApiV1ProvidersUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_update_kind_error_component import ApiV1ProvidersUpdateKindErrorComponent
        from ..models.api_v1_providers_update_labels_error_component import ApiV1ProvidersUpdateLabelsErrorComponent
        from ..models.api_v1_providers_update_legal_name_error_component import (
            ApiV1ProvidersUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_update_name_error_component import ApiV1ProvidersUpdateNameErrorComponent
        from ..models.api_v1_providers_update_non_field_errors_error_component import (
            ApiV1ProvidersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_update_phone_error_component import ApiV1ProvidersUpdatePhoneErrorComponent
        from ..models.api_v1_providers_update_platform_service_error_component import (
            ApiV1ProvidersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_update_provider_error_component import ApiV1ProvidersUpdateProviderErrorComponent
        from ..models.api_v1_providers_update_provider_id_error_component import (
            ApiV1ProvidersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_update_provider_reference_error_component import (
            ApiV1ProvidersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_update_reconciliation_enabled_error_component import (
            ApiV1ProvidersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_update_sla_availability_error_component import (
            ApiV1ProvidersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_sla_target_error_component import (
            ApiV1ProvidersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_update_slo_availability_error_component import (
            ApiV1ProvidersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_slo_target_error_component import (
            ApiV1ProvidersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_update_slug_error_component import ApiV1ProvidersUpdateSlugErrorComponent
        from ..models.api_v1_providers_update_target_availability_error_component import (
            ApiV1ProvidersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_update_tolerations_error_component import (
            ApiV1ProvidersUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_update_urls_error_component import ApiV1ProvidersUpdateUrlsErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersUpdateActiveErrorComponent
                | ApiV1ProvidersUpdateAddressErrorComponent
                | ApiV1ProvidersUpdateAnnotationsErrorComponent
                | ApiV1ProvidersUpdateArchivedAtErrorComponent
                | ApiV1ProvidersUpdateArchivedErrorComponent
                | ApiV1ProvidersUpdateArchivedReasonErrorComponent
                | ApiV1ProvidersUpdateAsnErrorComponent
                | ApiV1ProvidersUpdateCcmBlockErrorComponent
                | ApiV1ProvidersUpdateCertificationsErrorComponent
                | ApiV1ProvidersUpdateCriticalityErrorComponent
                | ApiV1ProvidersUpdateCsiControllerBlockErrorComponent
                | ApiV1ProvidersUpdateCsiStorageClassesErrorComponent
                | ApiV1ProvidersUpdateDebugModeErrorComponent
                | ApiV1ProvidersUpdateDisplayNameErrorComponent
                | ApiV1ProvidersUpdateEmailsErrorComponent
                | ApiV1ProvidersUpdateIconContentTypeErrorComponent
                | ApiV1ProvidersUpdateIconFilenameErrorComponent
                | ApiV1ProvidersUpdateKindErrorComponent
                | ApiV1ProvidersUpdateLabelsErrorComponent
                | ApiV1ProvidersUpdateLegalNameErrorComponent
                | ApiV1ProvidersUpdateNameErrorComponent
                | ApiV1ProvidersUpdateNonFieldErrorsErrorComponent
                | ApiV1ProvidersUpdatePhoneErrorComponent
                | ApiV1ProvidersUpdatePlatformServiceErrorComponent
                | ApiV1ProvidersUpdateProviderErrorComponent
                | ApiV1ProvidersUpdateProviderIdErrorComponent
                | ApiV1ProvidersUpdateProviderReferenceErrorComponent
                | ApiV1ProvidersUpdateReconciliationEnabledErrorComponent
                | ApiV1ProvidersUpdateSlaAvailabilityErrorComponent
                | ApiV1ProvidersUpdateSlaTargetErrorComponent
                | ApiV1ProvidersUpdateSloAvailabilityErrorComponent
                | ApiV1ProvidersUpdateSloTargetErrorComponent
                | ApiV1ProvidersUpdateSlugErrorComponent
                | ApiV1ProvidersUpdateTargetAvailabilityErrorComponent
                | ApiV1ProvidersUpdateTolerationsErrorComponent
                | ApiV1ProvidersUpdateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_0 = (
                        ApiV1ProvidersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_1 = (
                        ApiV1ProvidersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_2 = (
                        ApiV1ProvidersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_3 = (
                        ApiV1ProvidersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_4 = (
                        ApiV1ProvidersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_5 = (
                        ApiV1ProvidersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_6 = (
                        ApiV1ProvidersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_7 = (
                        ApiV1ProvidersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_8 = (
                        ApiV1ProvidersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_9 = (
                        ApiV1ProvidersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_10 = (
                        ApiV1ProvidersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_11 = (
                        ApiV1ProvidersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_12 = (
                        ApiV1ProvidersUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_13 = (
                        ApiV1ProvidersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_14 = (
                        ApiV1ProvidersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_15 = (
                        ApiV1ProvidersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_16 = (
                        ApiV1ProvidersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_17 = (
                        ApiV1ProvidersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_18 = (
                        ApiV1ProvidersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_19 = (
                        ApiV1ProvidersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_20 = (
                        ApiV1ProvidersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_21 = (
                        ApiV1ProvidersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_22 = (
                        ApiV1ProvidersUpdateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_23 = (
                        ApiV1ProvidersUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_24 = (
                        ApiV1ProvidersUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_25 = (
                        ApiV1ProvidersUpdateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_26 = (
                        ApiV1ProvidersUpdateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_27 = (
                        ApiV1ProvidersUpdateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_28 = (
                        ApiV1ProvidersUpdateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_29 = (
                        ApiV1ProvidersUpdateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_30 = (
                        ApiV1ProvidersUpdateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_31 = (
                        ApiV1ProvidersUpdateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_32 = (
                        ApiV1ProvidersUpdatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_33 = (
                        ApiV1ProvidersUpdateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_update_error_type_34 = (
                        ApiV1ProvidersUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_update_error_type_35 = (
                    ApiV1ProvidersUpdateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_update_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_update_validation_error.additional_properties = d
        return api_v1_providers_update_validation_error

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
