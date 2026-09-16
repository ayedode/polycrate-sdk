from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_idp_identityproviders_create_annotations_error_component import (
        ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_archived_at_error_component import (
        ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_archived_error_component import (
        ApiV1IdpIdentityprovidersCreateArchivedErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_archived_reason_error_component import (
        ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_criticality_error_component import (
        ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_debug_mode_error_component import (
        ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_display_name_error_component import (
        ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_hostname_error_component import (
        ApiV1IdpIdentityprovidersCreateHostnameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_kind_error_component import (
        ApiV1IdpIdentityprovidersCreateKindErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_labels_error_component import (
        ApiV1IdpIdentityprovidersCreateLabelsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_name_error_component import (
        ApiV1IdpIdentityprovidersCreateNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_non_field_errors_error_component import (
        ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_platform_service_error_component import (
        ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_provider_error_component import (
        ApiV1IdpIdentityprovidersCreateProviderErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_provider_id_error_component import (
        ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_provider_reference_error_component import (
        ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_reconciliation_enabled_error_component import (
        ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_sla_availability_error_component import (
        ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_sla_target_error_component import (
        ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_slo_availability_error_component import (
        ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_slo_target_error_component import (
        ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_sync_mode_error_component import (
        ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_target_availability_error_component import (
        ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_create_tolerations_error_component import (
        ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IdpIdentityprovidersCreateValidationError")


@_attrs_define
class ApiV1IdpIdentityprovidersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent |
            ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent | ApiV1IdpIdentityprovidersCreateArchivedErrorComponent
            | ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent |
            ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent |
            ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent |
            ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent | ApiV1IdpIdentityprovidersCreateHostnameErrorComponent
            | ApiV1IdpIdentityprovidersCreateKindErrorComponent | ApiV1IdpIdentityprovidersCreateLabelsErrorComponent |
            ApiV1IdpIdentityprovidersCreateNameErrorComponent | ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent
            | ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent |
            ApiV1IdpIdentityprovidersCreateProviderErrorComponent | ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent
            | ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent |
            ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent |
            ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent |
            ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent | ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent |
            ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent
        | ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent
        | ApiV1IdpIdentityprovidersCreateArchivedErrorComponent
        | ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent
        | ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent
        | ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent
        | ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent
        | ApiV1IdpIdentityprovidersCreateHostnameErrorComponent
        | ApiV1IdpIdentityprovidersCreateKindErrorComponent
        | ApiV1IdpIdentityprovidersCreateLabelsErrorComponent
        | ApiV1IdpIdentityprovidersCreateNameErrorComponent
        | ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent
        | ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent
        | ApiV1IdpIdentityprovidersCreateProviderErrorComponent
        | ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent
        | ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent
        | ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent
        | ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent
        | ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent
        | ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent
        | ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_idp_identityproviders_create_annotations_error_component import (
            ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_at_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_criticality_error_component import (
            ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_display_name_error_component import (
            ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_hostname_error_component import (
            ApiV1IdpIdentityprovidersCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_kind_error_component import (
            ApiV1IdpIdentityprovidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_labels_error_component import (
            ApiV1IdpIdentityprovidersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_name_error_component import (
            ApiV1IdpIdentityprovidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_platform_service_error_component import (
            ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_id_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_sla_target_error_component import (
            ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_slo_target_error_component import (
            ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_target_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_tolerations_error_component import (
            ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersCreateHostnameErrorComponent):
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
        from ..models.api_v1_idp_identityproviders_create_annotations_error_component import (
            ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_at_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_criticality_error_component import (
            ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_display_name_error_component import (
            ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_hostname_error_component import (
            ApiV1IdpIdentityprovidersCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_kind_error_component import (
            ApiV1IdpIdentityprovidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_labels_error_component import (
            ApiV1IdpIdentityprovidersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_name_error_component import (
            ApiV1IdpIdentityprovidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_platform_service_error_component import (
            ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_id_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_sla_target_error_component import (
            ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_slo_target_error_component import (
            ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_sync_mode_error_component import (
            ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_target_availability_error_component import (
            ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_idp_identityproviders_create_tolerations_error_component import (
            ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent
                | ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent
                | ApiV1IdpIdentityprovidersCreateArchivedErrorComponent
                | ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent
                | ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent
                | ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent
                | ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent
                | ApiV1IdpIdentityprovidersCreateHostnameErrorComponent
                | ApiV1IdpIdentityprovidersCreateKindErrorComponent
                | ApiV1IdpIdentityprovidersCreateLabelsErrorComponent
                | ApiV1IdpIdentityprovidersCreateNameErrorComponent
                | ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent
                | ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent
                | ApiV1IdpIdentityprovidersCreateProviderErrorComponent
                | ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent
                | ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent
                | ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent
                | ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent
                | ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent
                | ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent
                | ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_0 = (
                        ApiV1IdpIdentityprovidersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_1 = (
                        ApiV1IdpIdentityprovidersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_2 = (
                        ApiV1IdpIdentityprovidersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_3 = (
                        ApiV1IdpIdentityprovidersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_4 = (
                        ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_5 = (
                        ApiV1IdpIdentityprovidersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_6 = (
                        ApiV1IdpIdentityprovidersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_7 = (
                        ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_8 = (
                        ApiV1IdpIdentityprovidersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_9 = (
                        ApiV1IdpIdentityprovidersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_10 = (
                        ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_11 = (
                        ApiV1IdpIdentityprovidersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_12 = (
                        ApiV1IdpIdentityprovidersCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_13 = (
                        ApiV1IdpIdentityprovidersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_14 = (
                        ApiV1IdpIdentityprovidersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_15 = (
                        ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_16 = (
                        ApiV1IdpIdentityprovidersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_17 = (
                        ApiV1IdpIdentityprovidersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_18 = (
                        ApiV1IdpIdentityprovidersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_19 = (
                        ApiV1IdpIdentityprovidersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_20 = (
                        ApiV1IdpIdentityprovidersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_21 = (
                        ApiV1IdpIdentityprovidersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_create_error_type_22 = (
                        ApiV1IdpIdentityprovidersCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_idp_identityproviders_create_error_type_23 = (
                    ApiV1IdpIdentityprovidersCreateSyncModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_idp_identityproviders_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_idp_identityproviders_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_idp_identityproviders_create_validation_error.additional_properties = d
        return api_v1_idp_identityproviders_create_validation_error

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
