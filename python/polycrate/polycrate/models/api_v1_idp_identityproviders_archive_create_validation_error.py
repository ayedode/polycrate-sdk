from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_idp_identityproviders_archive_create_annotations_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_archived_at_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_archived_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_archived_reason_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_criticality_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_debug_mode_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_display_name_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_hostname_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_kind_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_labels_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_name_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_non_field_errors_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_platform_service_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_provider_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_provider_id_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_provider_reference_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_reconciliation_enabled_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_sla_availability_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_sla_target_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_slo_availability_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_slo_target_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_sync_mode_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_target_availability_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_archive_create_tolerations_error_component import (
        ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IdpIdentityprovidersArchiveCreateValidationError")


@_attrs_define
class ApiV1IdpIdentityprovidersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_idp_identityproviders_archive_create_annotations_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_at_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_criticality_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_display_name_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_hostname_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_kind_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_labels_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_name_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_platform_service_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_id_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_sla_target_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_slo_target_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_target_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_tolerations_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent):
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
        from ..models.api_v1_idp_identityproviders_archive_create_annotations_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_at_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_criticality_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_display_name_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_hostname_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_kind_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_labels_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_name_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_platform_service_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_id_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_sla_target_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_slo_target_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_sync_mode_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_target_availability_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_archive_create_tolerations_error_component import (
            ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_0 = (
                        ApiV1IdpIdentityprovidersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_1 = (
                        ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_2 = (
                        ApiV1IdpIdentityprovidersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_3 = (
                        ApiV1IdpIdentityprovidersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_4 = (
                        ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_5 = (
                        ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_6 = (
                        ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_7 = (
                        ApiV1IdpIdentityprovidersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_8 = (
                        ApiV1IdpIdentityprovidersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_9 = (
                        ApiV1IdpIdentityprovidersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_10 = (
                        ApiV1IdpIdentityprovidersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_11 = (
                        ApiV1IdpIdentityprovidersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_12 = (
                        ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_13 = (
                        ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_14 = (
                        ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_15 = (
                        ApiV1IdpIdentityprovidersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_16 = (
                        ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_17 = (
                        ApiV1IdpIdentityprovidersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_18 = (
                        ApiV1IdpIdentityprovidersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_19 = (
                        ApiV1IdpIdentityprovidersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_20 = (
                        ApiV1IdpIdentityprovidersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_21 = (
                        ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_22 = (
                        ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_23 = (
                    ApiV1IdpIdentityprovidersArchiveCreateSyncModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_idp_identityproviders_archive_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_idp_identityproviders_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_idp_identityproviders_archive_create_validation_error.additional_properties = d
        return api_v1_idp_identityproviders_archive_create_validation_error

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
